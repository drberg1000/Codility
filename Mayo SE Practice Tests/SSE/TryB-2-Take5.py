# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# https://app.codility.com/c/feedback/4UM9RK-J2D/

import unittest
import sys


def solution(n):
    maxim = list(str(-sys.maxsize-1))
    for index, digit in enumerate(str(n)):
        current = list(str(n))
        if digit != '5':
            continue
        current.pop(index)
        if int(''.join(maxim)) < int(''.join(current)):
            maxim = current.copy()

    return int(''.join(maxim))


class TestSolution(unittest.TestCase):
    def tearDown(self):
        self.actual = solution(self.input)
        self.assertEqual(self.expected, self.actual)

    def test_example1(self):
        self.input = 15958
        self.expected = 1958

    def test_example2(self):
        self.input = -5859
        self.expected = -589

    def test_example3(self):
        self.input = -5000
        self.expected = 0

    def test_max(self):
        self.input = 999995
        self.expected = 99999

    def test_min(self):
        self.input = -999995
        self.expected = -99999

    def test_min_two_fives(self):
        self.input = -599995
        self.expected = -59999

    def test_max_two_fives(self):
        self.input = 599995
        self.expected = 99995
