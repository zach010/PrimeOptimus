# Multiprocessing Prime number finder written by: zachap@gmail.com Copyright 2018
import sys
import os
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
    text = "\rProgress: [{}] {:.0f}/10 {}".format(
        chr(9632) * block + chr(9633) * (bar_length - block),
        round(progress * 10, 0), status)
    sys.stdout.write(text)
    sys.stdout.flush()
    return


def prime_multiprocess(n, c, q):
    a, b, c = n[0], n[1], c
    for i in range(a, b):
        if c % i == 0:
            return q.put(0)
    return q.put(1)


def segregate(num, precision):
    mp.dps = precision
    num = int(mp.floor(mp.sqrt(num)) + 1)
    cores = processor_cnt
    if num <= processor_cnt:
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
        place += num_divs[seg]
        num_seg.append(place)
        seg += 1
    num_seg = [int(num_seg[i]) for i in range(len(num_seg))]
    return num_seg, cores


def initialize(numb_seg, cores, number):
    q_list = [(multiprocessing.Queue()) for _ in range(cores)]
    n_list = [[0 for _ in range(2)] for _ in range(cores)]
    const = number
    for s in range(cores):
        for ss in range(1, 2):
            n_list[s][ss] = numb_seg[s]
            n_list[s][ss - 1] = numb_seg[s - 1]
    n_list[0][0] = 2
    arg_list = [(n_list[args], const, q_list[args]) for args in range(cores)]
    processes = [multiprocessing.Process(target=prime_multiprocess, args=arg_list[args]) for args in range(cores)]
    for p in processes:
        p.daemon = True
        p.start()
    print('\r' + 'Calculating...')
    start_t = time.time()
    run, tps, sps = 1, 0, []
    data = [0 for _ in range(cores)]
    while run == 1:
        for gp in range(cores):
            if not q_list[gp].empty() and tps == 0:
                data[gp] = q_list[gp].get()
                progress_bar(cores, sum(data)), print(end='')
                if data[gp] == 0:
                    print('\rProgress: [' + chr(9632) * 10 + '] 10/10')
                    tps = 1
                if sum(data) == cores:
                    run = 0
            if tps == 1:
                for tp in range(cores):
                    processes[tp].terminate()
                    sps.append(1)
                if sum(sps) >= cores:
                    run = 0
    stop_t = time.time()
    t = stop_t - start_t
    number_len = len(str(number))
    if t < 60:
        print("\rFinished processing in %.1f seconds." % t)
        if sum(data) == cores:
            print("Number: " + str(number) + "\nPrime: Yes\nLength: " + str(number_len))
        else:
            print("Number: " + str(number) + "\nPrime: No\nLength: " + str(number_len))
    if t >= 60:
        s, m = t, 0
        while s >= 60:
            s, m = s - 60, m + 1
        t_str = 'minute'
        if m > 1:
            t_str = 'minutes'
        print("\rFinished processing in %.0f " % m, end=""), print("" + t_str + " and %.1f seconds." % s)
        if sum(data) == cores:
            print("Number: " + str(number) + "\nPrime: Yes\nLength: " + str(number_len))
        else:
            print("Number: " + str(number) + "\nPrime: No\nLength: " + str(number_len))
    return start_program('nother')


if __name__ == '__main__':
    processor_cnt = multiprocessing.cpu_count()
    print("Python version %s.%s.%s" % sys.version_info[:3], '(' + str(8 * struct.calcsize("P")) + '-bit)')
    print("\nThis computer-system has (" + str(processor_cnt) + ") logical processors initialized for this Prime task.")


    def start_program(another):
        question = input('Do you want to calculate if a' + str(another) + ' number is Prime? (y/n): ')
        if question.startswith(str('y')) or question.startswith(str('Y')):
            number = input('Enter number for Prime test: ')
            if number == '1':
                print("The number 1 is not considered Prime because it is a square of which all are not Prime.")
                return start_program('')
            try:
                print('\r' + 'Initializing.', end='')
                number = eval(number)
            except (SyntaxError, NameError, ValueError):
                return print("\rInvalid Input."), start_program('')
            try:
                precision = len(str(number)) + 4
                number = int(number)
                print('\r' + 'Initializing..', end='')
                num_segments, num_cores = segregate(number, precision)
                print('\r' + 'Initializing...', end='')
                initialize(num_segments, num_cores, number)
            except ValueError:
                print("Invalid Input.")
                return start_program('')
        elif question.startswith(str('n')) or question.startswith(str('N')):
            print("Program Exit."), os.system('cmd /k'), sys.exit()
        else:
            print("Invalid Input.")
            return start_program('')
    start_program('')
