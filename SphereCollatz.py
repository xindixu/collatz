#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # pre-condition
    assert isinstance(i, int), "argument(s) is not an int"
    assert isinstance(j, int), "argument(s) is not an int"

    if i > j:
        assert j > 0, "argument(s) out of range"
        assert i < 1000000, "argument(s) out of range"
        r = range(j, i+1)
    else:
        assert i > 0, "argument(s) out of range"
        assert j < 1000000, "argument(s) out of range"
        r = range(i, j+1)

    max_cyc_len = 0;

    for i in r:
        cyc_len = 1
        while i > 1:
            if i % 2 == 0:
                i = i >> 1
            else:
                i = 3 * i + 1
            cyc_len += 1;
        if max_cyc_len < cyc_len:
            max_cyc_len = cyc_len

    # post-condition
    assert max_cyc_len >= cyc_len, "max_cyc_len is less than one cyc_len"
    assert max_cyc_len >= 1, "max_cyc_len is less than 1"

    return max_cyc_len

# -------------
# collatz_print
# -------------

def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)

#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# ------------------------------

import sys

# ----
# main
# ----

if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
