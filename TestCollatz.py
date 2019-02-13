#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_use_cache
# from SphereCollatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_use_cache

import logging

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,10)
        self.assertEqual(j,1)

    def test_read_3(self):
        s = " 1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,1)
        self.assertEqual(j,10)

    def test_read_4(self):
        s = "1 10 \n"
        i, j = collatz_read(s)
        self.assertEqual(i,1)
        self.assertEqual(j,10)

    def test_read_5(self):
        s = "1  10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,1)
        self.assertEqual(j,10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6(self):
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    def test_eval_7(self):
        v = collatz_eval(5000, 10000)
        self.assertEqual(v, 262)

    def test_eval_8(self):
        try:
            v = collatz_eval(0,1000000)
        except AssertionError:
            # logging.error('\nfrom test_eval_8', exc_info=True)
            pass

    def test_eval_9(self):
        try:
            v = collatz_eval(1000000,0)
        except AssertionError:
            # logging.error('\nfrom test_eval_9', exc_info=True)
            pass

    # ----------------
    # eval_use_cache
    # ----------------

    def test_eval_use_cache_1(self):
        v = collatz_eval_use_cache(500,85500)
        self.assertEqual(v, 351)

    def test_eval_use_cache_2(self):
        v = collatz_eval_use_cache(500,652)
        self.assertEqual(v, 145)

    def test_eval_use_cache_3(self):
        v = collatz_eval_use_cache(1001,2002)
        self.assertEqual(v, 182)

    def test_eval_use_cache_4(self):
        v = collatz_eval_use_cache(10000,20020)
        self.assertEqual(v, 279)

    def test_eval_use_cache_5(self):
        v = collatz_eval_use_cache(20020,10000)
        self.assertEqual(v, 279)

    def test_eval_use_cache_6(self):
        v = collatz_eval_use_cache(39920,20332)
        self.assertEqual(v, 324)

    def test_eval_use_cache_7(self):
        v = collatz_eval_use_cache(92883, 123333)
        self.assertEqual(v, 354)

    def test_eval_use_cache_8(self):
        v = collatz_eval_use_cache(999999,1)
        self.assertEqual(v, 525)

    def test_eval_use_cache_9(self):
        v = collatz_eval_use_cache(50000,6000)
        self.assertEqual(v, 324)

    def test_eval_use_cache_10(self):
        v = collatz_eval_use_cache(4000,999999)
        self.assertEqual(v, 525)

    def test_eval_use_cache_11(self):
        v = collatz_eval_use_cache(30098,33203)
        self.assertEqual(v, 285)

    def test_eval_use_cache_12(self):
        v = collatz_eval_use_cache(12332, 222222)
        self.assertEqual(v, 386)

    def test_eval_use_cache_13(self):
        v = collatz_eval_use_cache(4379, 6171)
        self.assertEqual(v, 262)

    def test_eval_use_cache_14(self):
        v = collatz_eval_use_cache(4379, 6170)
        self.assertEqual(v, 236)

    def test_eval_use_cache_15(self):
        v = collatz_eval_use_cache(4379, 6172)
        self.assertEqual(v, 262)

    def test_eval_use_cache_16(self):
        v = collatz_eval_use_cache(127097, 128251)
        self.assertEqual(v, 331)

    def test_eval_use_cache_17(self):
        v = collatz_eval_use_cache(128251, 129993)
        self.assertEqual(v, 344)

    def test_eval_use_cache_18(self):
        v = collatz_eval_use_cache(127097, 129990)
        self.assertEqual(v, 331)

    def test_eval_use_cache_19(self):
        v = collatz_eval_use_cache(873300,390)
        self.assertEqual(v, 525)


    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 10, 20)
        self.assertEqual(w.getvalue(), "10 10 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 20321, 21033, 89)
        self.assertEqual(w.getvalue(), "20321 21033 89\n")
    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
        w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    def test_solve_2(self):
        r = StringIO("10 10 \n10    1\n 992 222\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
        w.getvalue(), "10 10 7\n10 1 20\n992 222 179\n")

    def test_solve_3(self):
        r = StringIO("999999 1\n2 80000\n80000 2\n3 4\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "999999 1 525\n2 80000 351\n80000 2 351\n3 4 8\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


% coverage report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
