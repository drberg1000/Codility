# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")a
# This answer only got a 55%.
# 3/6 correctness test cases passed.  1/7 performance test cases passed
# https://app.codility.com/c/feedback/4UM9RK-J2D/

import unittest
from collections import defaultdict


def solution_orig(s):
    counts = defaultdict(lambda: 0)
    for char in s:
        counts[char] += 1
    sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)}

    head = list()
    middle = ''
    for k, v in sorted_counts.items():
        while v >= 2:
            head.append(k)
            v -= 2
        if v == 1:
            middle = k
            break

    while len(head) > 0 and head[0] == '0':
        head.pop(0)

    if len(head) == 0 and middle == '':
        return '0'

    return ''.join(head) + middle + ''.join(reversed(head))


# This version is significnatly faster than solution_orig (200ms->7ms)
# I assume it still has the same correctness issues though.
# noinspection DuplicatedCode
def solution_improved(s):
    counts = defaultdict(lambda: 0)
    for char in s:
        counts[char] += 1
    sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: (item[0], item[1]), reverse=True)}

    head = list()
    middle = ''
    for k, v in sorted_counts.items():
        if v % 2 == 1 and middle == '':
            middle = k
            v -= 1
        # Don't fill head with nothing
        if k == '0' and len(head) == 0:
            break
        while v >= 2:
            head.append(k)
            v -= 2

    if len(head) == 0 and middle == '':
        return '0'

    return ''.join(head) + middle + ''.join(reversed(head))


def solution(s):
    return solution_improved(s)


class TestSolution(unittest.TestCase):
    def tearDown(self):
        self.assertEqual(self.expected, self.actual)

    def test_example1(self):
        self.expected = '898'
        self.actual = solution('39878')

    def test_example2(self):
        self.expected = '9'
        self.actual = solution('00900')

    def test_example3(self):
        self.expected = '0'
        self.actual = solution('0000')

    def test_example4(self):
        self.expected = '5'
        self.actual = solution('54321')

    def test_longest_zeros(self):
        self.expected = '0'
        self.actual = solution('0' * 100000)

    def test_longest_nines(self):
        self.expected = '9' * 100000
        self.actual = solution('9' * 100000)

    def test_longest_odd_nines(self):
        self.expected = '9' * 99999
        self.actual = solution('9' * 99999)

    # Added these after submission
    def test_2_lowest_in_middle_and_ends(self):
        self.expected = '98889'
        self.actual = solution('89898')

    def test_2_biggest_in_middle(self):
        self.expected = '898'
        self.actual = solution('889')

    def test_2_zero_in_head(self):
        self.expected = '10901'
        self.actual = solution('90011')
