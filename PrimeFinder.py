# Multiprocessing prime number finder
# Written by: Zachary Alexander Pettibone
# Email: zachap@gmail.com Copyright 2020
import sys
import struct
import time
from mpmath import mp
import multiprocessing


def progress_bar(total, progress):
    bar_length, status = 10, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(bar_length * progress))
    text = "\rProgress: {}".format(
        "#" * block + "=" * (bar_length - block), round(progress * 10, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
    return


def prime_multiprocess(n, c, q):
    a, b, c = n[0], n[1], c
    
    for i in range(a, b):
        if c % i == 0:
            return q.put(0)
    return q.put(1)


def prime_probability_multiprocess(n, c, q, t):
    a, b, c = n[0], n[1], c
    t = t + a
    for i in range(a, b):
        if c % i == 0:
            return q.put(0)
        if i > t:
            return q.put(1)
    return q.put(1)


def segregate(num, precision):
    mp.dps = precision
    num = int(mp.floor(mp.sqrt(num)) + 1)
    cores = pro_cnt
    if num <= pro_cnt:
        cores = num - 1
    num_mod = mp.fmod(num, cores)
    num_mods = [1 for _ in mp.arange(num_mod)]
    while len(num_mods) < cores:
        num_mods.append(0)
    num_div = mp.floor(mp.fdiv(num, cores))
    num_divs, ip = [], 0
    while len(num_divs) < cores:
        num_divs.append(num_div + num_mods[ip])
        ip += 1
    num_seg, place, seg = [num_divs[0]], num_divs[0], 1
    while len(num_seg) < cores:
        place += (num_divs[seg])
        num_seg.append(place)
        seg += 1
    num_seg = [int(num_seg[i]) for i in range(len(num_seg))]
    return num_seg, cores


def initialize(numb_seg, cores, number, probable, t_check):
    q_list = [(multiprocessing.Queue()) for _ in range(cores)]
    n_list = [[0 for _ in range(2)] for _ in range(cores)]
    const = number
    for s in range(cores):
        for ss in range(1, 2):
            n_list[s][ss] = numb_seg[s]
            n_list[s][ss - 1] = numb_seg[s - 1]
    n_list[0][0] = 2
    if probable == 0:
        arg_list = [(n_list[args], const, q_list[args]) for args in range(cores)]
        processes = [multiprocessing.Process(target=prime_multiprocess, args=arg_list[args]) for args in range(cores)]
        for p in processes:
            p.daemon = True
            p.start()
        run, tps, sps = 1, 0, []
        data = [0 for _ in range(cores)]
        while run == 1:
            for gp in range(cores):
                if not q_list[gp].empty() and tps == 0:
                    data[gp] = q_list[gp].get()
                    if data[gp] == 0:
                        tps = 1
                    if sum(data) == cores:
                        run = 0
                if tps == 1:
                    for tp in range(cores):
                        processes[tp].terminate()
                        sps.append(1)
                    if sum(sps) >= cores:
                        run = 0
        if sum(data) == cores:
            return number

    if probable == 1:
        arg_list = [(n_list[args], const, q_list[args], t_check) for args in range(cores)]
        processes = [multiprocessing.Process(target=prime_probability_multiprocess,
                                             args=arg_list[args]) for args in range(cores)]
        for p in processes:
            p.daemon = True
            p.start()
        run, tps, sps = 1, 0, []
        data = [0 for _ in range(cores)]
        while run == 1:
            for gp in range(cores):
                if not q_list[gp].empty() and tps == 0:
                    data[gp] = q_list[gp].get()
                    if data[gp] == 0:
                        tps = 1
                    if sum(data) == cores:
                        run = 0
                if tps == 1:
                    for tp in range(cores):
                        processes[tp].terminate()
                        sps.append(1)
                    if sum(sps) >= cores:
                        run = 0
        if sum(data) == cores:
            return number


def probability():
    global skip
    probable = input('Do you want to test for probable primes?: ')
    if probable.startswith(str('y')) or probable.startswith(str('Y')):
        information = \
              '\nHow many loop-steps do you want a multiprocess to continue to\n' \
              'multi-core-sample a number that has not found an immediate factor?\n' \
              'Larger numbers increase odds of finding a \'more potential\' prime.\n' \
              'Can be entered as (2**23) where (**) is raising to the exponent.\n'
        for read in information:
            print(read, end='')
            if skip == 0:
                time.sleep(0.04)
            if skip == 1:
                time.sleep(0.00)
        time.sleep(0.5)
        skip = 1
        t_limit = input('Maximum multiprocess STEPS: ')
        try:
            t_limit = eval(t_limit)
            return 1, int(int(t_limit))
        except (SyntaxError, NameError, ValueError):
            return print("\rInvalid Input."), probability()
    if probable.startswith(str('n')) or probable.startswith(str('N')):
        return 0, 0
    else:
        return print("\rInvalid Input."), probability()


if __name__ == '__main__':
    pro_cnt = multiprocessing.cpu_count()
    skip = 0
    print('\nPython version %s.%s.%s' % sys.version_info[:3], ' (' + str(8 * struct.calcsize("P")) + '-bit)\n'
          'This computer-system has (' + str(pro_cnt) + ') logical processors for this prime task.\n'
          'This is a multiprocessing prime number program written by zachap@gmail.com.\n'    
          'A single number will be evenly split (' + str(pro_cnt) + ') times across its domain to be sampled\n'
          'by simultaneous calculations on separate cores checking the number for factors.\n')

    def start_program():
        print('\r' + 'Initializing...', end='\n')
        prime_list = []
        probable, t_limit = probability()

        try:
            print("\nExamples of prime number functions in python: \n"
                  "Kynea primes: (2**n+1)**2-2\n"
                  "Mersenne primes: (2**n)-1\n"
                  "Zach primes: 2*(n**2)-1\n")
            function = input('Enter prime number FUNCTION:')
            if 'n' in function:
                eval(function.replace('n', '0'))
            else:
                return print("\rInvalid Input."), start_program()
            start_function = input('Enter the number for \'n\' START:')
            start_function = eval(start_function)
            iterations = int(input('Enter the number of ITERATIONS:'))
            start_t = time.time()
        except (SyntaxError, NameError, ValueError):
            return print("\rInvalid Input."), start_program()

        if probable == 0:
            for n in range(start_function, iterations):
                it = eval(function.replace('n', '' + str(n) + ''))
                precision = len(str(it)) + 4
                num_segments, num_cores = segregate(it, precision)
                t_prime = initialize(num_segments, num_cores, it, probable, t_limit)
                progress_bar((int(iterations)), n - start_function)
                if n < 2 ** 800:
                    sys.stdout.write(' n=' + str(n + 1) + ' (Primes found: ' + str(len(prime_list)) + ')')
                    sys.stdout.flush()
                if n > 2 ** 800:
                    sys.stdout.write(' (Primes found: ' + str(len(prime_list)) + ')')
                    sys.stdout.flush()
                if t_prime is not None:
                    prime_list.append(str('ƒ(' + str(n) + ') = ' + str(t_prime) + ''))
                    if prime_list[0] == 'ƒ(1) = 1':
                        del prime_list[0]

        if probable == 1:
            for n in range(start_function, iterations):
                it = eval(function.replace('n', '' + str(n) + ''))
                precision = len(str(it)) + 4
                num_segments, num_cores = segregate(it, precision)
                t_prime = initialize(num_segments, num_cores, it, probable, t_limit)
                progress_bar((int(iterations)), n - start_function)
                if n < 2 ** 800:
                    sys.stdout.write(' n=' + str(n + 1) + ' (Potential primes found: ' + str(len(prime_list)) + ')')
                    sys.stdout.flush()
                if n > 2 ** 800:
                    sys.stdout.write(' (Potential primes found: ' + str(len(prime_list)) + ')')
                    sys.stdout.flush()
                if t_prime is not None:
                    prime_list.append(str('ƒ(' + str(n) + ') = ' + str(t_prime) + ''))
                    if prime_list[0] == 'ƒ(1) = 1':
                        del prime_list[0]
        stop_t = time.time()
        t = stop_t - start_t

        if probable == 0:
            progress_bar(1, 1), print(' 100%', end='')
            print('\nPrimes:')
            if len(prime_list) >= 1:
                print(('\n'.join(map(str, prime_list))))
                if prime_list is not None:
                    print('Primes found: ' + str(len(prime_list)) + '')
                    p_len = len(prime_list[-1]) - (prime_list[-1].index('=') + 2)
                    print('Prime at end of list has ' + str(p_len) + ' digits.')
            else:
                print(prime_list)
        if probable == 1:
            progress_bar(1, 1), print(' 100%', end='')
            print('\nPotential primes:')
            if len(prime_list) >= 1:
                print(('\n'.join(map(str, prime_list))))
                if prime_list is not None:
                    print('\'Potential\' primes found: ' + str(len(prime_list)) + '')
                    p_len = len(prime_list[-1]) - (prime_list[-1].index('=') + 2)
                    print('\'Potential\' prime at end of list has ' + str(p_len) + ' digits.')
            else:
                print(prime_list)
        if t < 60:
            print("\rOverall process took %.1f seconds." % t)
        if t >= 60:
            s, m = t, 0
            while s >= 60:
                s, m = s - 60, m + 1
            t_str = 'minute'
            if m > 1:
                t_str = 'minutes'
            print("\rOverall process took %.0f " % m, end=""), print("" + t_str + " and %.1f seconds." % s)
        start_program()
    start_program()
