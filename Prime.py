# Multiprocessing Prime number finder written by: zachap@gmail.com Copyright 2018
import sys
import os
import struct
import time
import math
from mpmath import mp
import multiprocessing
from multiprocessing import Barrier


def progress_bar(total, progress):
    bar_length, status = 10, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(bar_length * progress))
    text = "\rProgress: ►{}◄ {:.0f}/10 {}".format(
        "■" * block + "□" * (bar_length - block), round(progress * 10, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()
    return


def prime_multiprocess(n, s, q, t, c, p):
    s.wait()
    const = int(n[2])
    mp.dps = p + 4
    ia = int(mp.floor(mp.sqrt(n[0])))
    ib = int(mp.floor(mp.sqrt(n[1])) + 1)
    ic = int(mp.floor(mp.sqrt(n[2])) + 1)
    ix, iz = 0, 0
    ld = int((mp.mpf(ib) / mp.mpf(c)) + 1)
    if ia == 1:
        for i in range(ia, ic):
            if const % i == 0:
                iz += 1
                if iz > 1:
                    return q.put(0)
            if i > ib and iz < 2:
                return q.put(1)
            if i % ld == 0:
                ix += 1
                t.put(ix)
        return q.put(1)
    else:
        for i in range(ia, ic):
            if const % i == 0:
                iz += 1
                if iz > 1:
                    return q.put(0)
            if i > ib and iz < 2:
                return q.put(1)
        return q.put(1)


def segregate(num):
    cores = processor_cnt
    if num <= processor_cnt:
        cores = int(num) - 1
    num_mod = mp.fmod(int(num), cores)
    num_mods = [1 for _ in mp.arange(num_mod)]
    while len(num_mods) < cores:
        num_mods.append(0)
    num_div = mp.floor(mp.fdiv(num, cores))
    num_divs = []
    ip = 0
    while len(num_divs) < cores:
        num_divs.append(num_div + num_mods[ip])
        ip += 1
    num_seg = [num_divs[0]]
    seg = 1
    place = num_divs[0]
    while len(num_seg) < cores:
        place += (num_divs[seg])
        num_seg.append(place)
        seg += 1
    return num_seg, cores


def initialize(numb_seg, cores, number, precision):
    sync = Barrier(cores)
    q_list = [(multiprocessing.Queue()) for _ in range(cores)]
    t_list = [multiprocessing.Queue()]
    n_list = [[0 for _ in range(3)] for _ in range(cores)]
    mpf_number = mp.mpf(number)
    for s in range(cores):
        for ss in range(1, 2):
            n_list[s][ss+1] = mpf_number
            n_list[s][ss] = numb_seg[s]
            n_list[s][ss - 1] = numb_seg[s - 1] + 1
    n_list[0][0] = mp.mpf(1)
    arg_list = [(n_list[args], sync, q_list[args], t_list[0], cores, precision) for args in range(cores)]
    processes = [multiprocessing.Process(target=prime_multiprocess, args=arg_list[args]) for args in range(cores)]
    for p in processes:
        p.daemon = True
        p.start()
    print('\r' + 'Calculating...')
    start_t = time.time()
    run, tps, sps = 1, 0, []
    data = [0 for _ in range(cores)]
    while run == 1:
        if not t_list[0].empty():
            x = t_list[0].get()
            if x <= cores:
                progress_bar(cores, x + 1)
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
    stop_t = time.time()
    t_sum = stop_t - start_t
    number_len = str(len(str(int(number))))
    if t_sum < 60:
        print("\rFinished processing in %.1f seconds." % t_sum)
        if sum(data) == cores:
            print("Number: " + str(number) + "\nPrime: Yes\nLength: " + number_len)
        else:
            print("Number: " + str(number) + "\nPrime: No\nLength: " + number_len)
    if t_sum >= 60:
        t_num = t_sum / 60
        t_dec = format((t_num - math.floor(t_num)) * 60, '.3g')
        t_min = 'minute'
        if (t_sum / 60) >= 2:
            t_min = 'minutes'
        print("\rFinished processing in %.0f " % t_num,
              end=""), print("" + t_min + " and " + t_dec + " seconds.")
        if sum(data) == cores:
            print("Number: " + str(number) + "\nPrime: Yes\nLength: " + number_len)
        else:
            print("Number: " + str(number) + "\nPrime: No\nLength: " + number_len)
    return start_program('nother')


if __name__ == '__main__':
    processor_cnt = multiprocessing.cpu_count()
    print("Python version %s.%s.%s" % sys.version_info[:3], '(' + str(8 * struct.calcsize("P")) + '-bit)')
    print("\nThis computer-system has (" + str(processor_cnt) + ") logical processors initialized for this Prime task.")


    def start_program(another):
        s_n = 0
        single = input('Do you want to calculate if a' + str(another) + ' number is Prime? (y/n): ')
        if single.startswith(str('y')) or single.startswith(str('Y')):
            number = input('Enter the number for a Prime check : ')
            print('\r' + 'Initializing...', end='')
            if number.__contains__('e'):
                s_n = 1
            elif number.__contains__('^'):
                add, sub = 0, 0
                exp = number.find('^')
                if number.__contains__('-'):
                    sub = number.find('-')
                    a_s = number.find('-')
                elif number.__contains__('+'):
                    add = number.find('+')
                    a_s = number.find('+')
                else:
                    a_s = len(number)
                head = ''.join([number[l] for l in range(0, exp)])
                tail = ''.join([number[t] for t in range(exp + 1, a_s)])
                a_or_s = ''.join([number[aos] for aos in range(a_s + 1, len(number))])
                if add > 0:
                    try:
                        number = (int(head) ** int(tail)) + int(a_or_s)
                        mp.dps = len(str(number + 8))
                    except ValueError:
                        print("Invalid Input.")
                        return start_program('')
                elif sub > 0:
                    try:
                        number = (int(head) ** int(tail)) - int(a_or_s)
                        mp.dps = len(str(number + 8))
                    except ValueError:
                        print("Invalid Input.")
                        return start_program('')
                else:
                    try:
                        number = int(head) ** int(tail)
                        mp.dps = len(str(number + 8))
                    except ValueError:
                        print("Invalid Input.")
                        return start_program('')
            try:
                if s_n == 1:
                    number = mp.mpf(number)
                else:
                    number = int(number)
            except ValueError:
                print("Invalid Input.")
                return start_program('')
            if s_n == 1:
                number = int(number)
                precision = len(str(number + 10))
                number = mp.mpf(number)
            else:
                number = int(number)
                precision = len(str(number + 10))
            if number == mp.mpf(1):
                print("The number 1 is not considered Prime because it is a square of which all are not Prime.")
            else:
                num_segments, num_cores = segregate(number)
                initialize(num_segments, num_cores, number, precision)
        elif single.startswith(str('n')) or single.startswith(str('N')):
            print("Program Exit.")
            os.system('cmd /k'), sys.exit()
        else:
            print("Invalid Input.")
            return start_program('')
    start_program('')
