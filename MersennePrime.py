# Lucas Lehmer Mersenne prime finding method
# Written by Zachary Alexander Pettibone
# August 2, 2020
# Email: zachap@gmail.com
import time
import sys


def progress_bar(t, p):
    bar_len, s = 10, ""
    p = float(p) / float(t)
    if p >= 1.:
        p, s = 1, "\r\n"
    block = int(round(bar_len * p))
    text = "\rProgress: {} {:.0f}% {}".format(
        "■" * block + "□" * (bar_len - block), round(p * 100, 0),
        s)
    sys.stdout.write(text)
    sys.stdout.flush()
    return


def check_level(y):
    lucas = 4
    while lucas < y:
        lucas = (lucas**2) - 2
    return lucas % y


# p = function total, n = function input, t = lucas start
def lucas_lehmer(p, n, t):
    for c in range(0, n):
        progress_bar(n, c)
        t = (t ** 2) - 2
        t = t % p
        if c >= n-1:
            progress_bar(10, 10)
            return 0
        if t == 0:
            progress_bar(10, 10)
            return 1


if __name__ == '__main__':
    def run_program():
        try:
            x = int(input('For Mersenne (2^n)-1 enter ƒ(n):'))
            y = (2**x)-1
            len_y = len(str(y))
            1/y
            start_t = time.time()
            c = check_level(y)
            a = lucas_lehmer(y, x, c)
            stop_t = time.time()
            ti = stop_t - start_t
            if a == 0:
                print('(2^' + str(x) + ')-1\nPrime: NO.')
                print('Length: ' + str(len_y) + ' digits.')
            if a == 1:
                print('(2^' + str(x) + ')-1\nPrime: YES.')
                print('Length: ' + str(len_y) + ' digits.')
            if ti < 60:
                print("\rOverall process took: %.1f seconds." % ti)
            if ti >= 60:
                s, m = ti, 0
                while s >= 60:
                    s, m = s - 60, m + 1
                t_str = 'minute'
                if m > 1:
                    t_str = 'minutes'
                print("\rOverall process took: %.0f " % m, end=""), print("" + t_str + " and %.1f seconds." % s)
            run_program()
        except Exception as ex:
            ex = str(ex)
            ex = str(ex[0].upper()+ex[1:])
            print('Error: ' + str(ex) + '.')
            run_program()
    run_program()
