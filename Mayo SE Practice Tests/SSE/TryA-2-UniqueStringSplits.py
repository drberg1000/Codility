# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import unittest


def solution(s):
    this_substring = set()
    substring_count = 1

    for char in s:
        if char in this_substring:
            this_substring.clear()
            substring_count += 1
        this_substring.add(char)

    return substring_count


class TestSolution(unittest.TestCase):
    def test_example1(self):
        self.input = 'world'
        self.expected_output = 1

    def test_example2(self):
        self.input = 'dddd'
        self.expected_output = 4

    def test_example3(self):
        self.input = 'cycle'
        self.expected_output = 2

    def test_example4(self):
        self.input = 'abba'
        self.expected_output = 2

    def test_longest_string(self):
        self.input = 'abcdefgh' * 250000
        self.expected_output = 250000

    def tearDown(self):
        actual = solution(self.input)
        self.assertEqual(self.expected_output, actual)
