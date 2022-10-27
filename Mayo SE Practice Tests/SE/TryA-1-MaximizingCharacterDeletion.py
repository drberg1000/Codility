# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import unittest


def solution(s):
    # write your code in Python 3.8.10
    for index in range(len(s)-1):
        if s[index] > s[index+1]:
            return s[:index] + s[index+1:]
    return s[:-1]


class TestSolution(unittest.TestCase):
    def test_example1(self):
        expected = 'ab'
        actual = solution('abc')

        self.assertEqual(expected, actual)

    def test_example2(self):
        expected = 'cdility'
        actual = solution('codility')

        self.assertEqual(expected, actual)

    def test_example3(self):
        expected = 'aaa'
        actual = solution('aaaa')

        self.assertEqual(expected, actual)

    def test_large_string(self):
        expected = 'aad' + 'azad' * int(100000/4-1)
        actual = solution('azad' * int(100000/4))

        self.assertEqual(expected, actual)

    def test_drop_first_character(self):
        expected = 'ba'
        actual = solution('cba')

        self.assertEqual(expected, actual)
