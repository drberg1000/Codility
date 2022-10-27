# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import unittest
import math


def solution(s):
    turn = {
        'B': 1,
        'N': 2,
        'A': 3,
    }
    counts = {
        'B': 0,
        'N': 0,
        'A': 0,
    }
    for char in s:
        try:
            counts[char]+=1
        except KeyError:
            pass
    turns = 100000  # longest string gives an upper bound on possible # of turns
    for k, v in turn.items():
        turns = min(math.floor(counts[k] / v), turns)

    return turns


class TestSolution(unittest.TestCase):
    def tearDown(self):
        self.assertEqual(self.expected, self.actual)

    def test_example1(self):
        self.expected = 1
        self.actual = solution('NAABXXAN')

    def test_example2(self):
        self.expected = 2
        self.actual = solution('NAANAAXNABABYNNBZ')

    def test_example3(self):
        self.expected = 0
        self.actual = solution('QABAAAWOBL')

    def test_large_string_max_turns(self):
        s = 'BNNAAA' * math.floor(100000/6)
        self.expected = math.floor(100000/6)
        self.actual = solution(s)

    def test_large_string_no_turns(self):
        # Checking that performance is reasonable with 100000 characters
        # Humorous that the longest string taht's an acceptable input for the function is not acceptable for a test case.
        s = 'bnnaaa' * math.floor(100000/6)
        self.expected = 0
        self.actual = solution(s)
