# Multiprocessing Prime number finder written by zachap@gmail.com Copyright 2018
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


def prime_multiprocess(n, s, q, p, t):
    s.wait()
    const = int(n[2])
    ia = int(mp.floor(mp.sqrt(n[0])))
    ib = int(mp.floor(mp.sqrt(n[1])) + 1)
    ic = int(mp.floor(mp.sqrt(n[2])) + 1)
    ix, iz = 0, 0
    mp.dps = len(str(ic))
    ld = int((mp.mpf(ib) / mp.mpf(10)) + 1)
    for i in range(ia, ic):
        if const % i == 0:
            iz += 1
            if iz > 1:
                return q.put(0)
        if i > ib and iz < 2:
            return q.put(1)
        if p == 0:
            if i % ld == 0:
                ix += 1
                t.put(ix)
    return q.put(1)


def split(num):
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


def initialize(numb_seg, cores, number):
    sync = Barrier(cores)
    q_list = [(multiprocessing.Queue()) for _ in range(cores)]
    t_list = [multiprocessing.Queue()]
    n_list = [[0 for _ in range(3)] for _ in range(cores)]
    p_list = [c for c in range(cores)]
    for s in range(cores):
        for ss in range(1, 2):
            n_list[s][ss+1] = mp.mpf(number)
            n_list[s][ss] = numb_seg[s]
            n_list[s][ss - 1] = numb_seg[s - 1] + 1
    n_list[0][0] = mp.mpf(1)
    # print(n_list)
    mp.dps = 512
    arg_list = [(n_list[args], sync, q_list[args], p_list[args], t_list[0]) for args in range(cores)]
    processes = [multiprocessing.Process(target=prime_multiprocess, args=arg_list[args]) for args in range(cores)]
    for p in processes:
        p.daemon = True
        p.start()
    print(end=''), print('\r' + 'Calculating...  ')
    start_t = time.time()
    run, tps, sps = 1, 0, []
    data = [0 for _ in range(cores)]
    while run == 1:
        if not t_list[0].empty():
            x = t_list[0].get()
            if x <= cores + 1:
                progress_bar(cores, x - 1)
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
    answer_bits = data
    stop_t = time.time()
    d_sum = stop_t - start_t
    if d_sum < 60:
        print("\rFinished processing (" + str(number) + ") in %.1f seconds." % d_sum)
        if sum(answer_bits) == cores:
            print("" + str(number) + " is Prime.")
            os.system('cmd /k')
        else:
            print("" + str(number) + " is not Prime.")
            os.system('cmd /k')
    if d_sum >= 60:
        d_num = d_sum / 60
        d_dec = format((d_num - math.floor(d_num)) * 60, '.3g')
        d_min = 'minute'
        if (d_sum / 60) >= 2:
            d_min = 'minutes'
        print("\rFinished processing (" + str(number) + ") in %.0f " % d_num,
              end=""), print("" + d_min + " and " + d_dec + " seconds.")
        if sum(answer_bits) == cores:
            print("" + str(number) + " is Prime.")
            os.system('cmd /k')
        else:
            print("" + str(number) + " is not Prime.")
            os.system('cmd /k')
        return


if __name__ == '__main__':
    processor_cnt = multiprocessing.cpu_count()
    print("Python version %s.%s.%s" % sys.version_info[:3], '(' + str(8 * struct.calcsize("P")) + '-bit)')
    print("\nThis computer-system has (" + str(processor_cnt) + ") logical processors initialized for this Prime task.")


    def start_program():
        single = input('Do you want to calculate if a number is Prime? (y/n): ')
        if single.startswith(str('y')) or single.startswith(str('Y')):
            number = input('Enter the number for a Prime check : ')
            try:
                number = int(number)
            except ValueError:
                print("Invalid Input.")
                start_program()
            mp.dps = len(str(number))
            number = mp.mpf(number)
            if number == mp.mpf(1):
                print("The number 1 is not considered Prime because it is a square of which all are not Prime.")
            elif number == mp.mpf(2):
                print("2 is the only even Prime number. Its not square and its only divisible by 1 and itself.")
            else:
                num_segments, num_cores = split(number)
                initialize(num_segments, num_cores, number)
        elif single.startswith(str('n')) or single.startswith(str('N')):
            print("Program Exit.")
        else:
            print("Invalid Input.")
            start_program()
    start_program()
