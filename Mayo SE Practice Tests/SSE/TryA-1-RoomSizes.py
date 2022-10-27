# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import unittest


def solution(a):
    rooms_needed = 0
    # Reversing speeds things up from >1s to 43ms for input [1]*100000
    a.sort(reverse=True)
    while len(a):
        rooms_needed += 1
        try:
            # Popping instead of indexing speeds up another 10ms.
            for _ in range(a.pop() - 1):
                a.pop()
        except IndexError:
            pass
    return rooms_needed


class TestSolution(unittest.TestCase):
    def test_example1(self):
        self.input = [1, 1, 1, 1, 1]
        self.expected_output = 5

    def test_example2(self):
        self.input = [2, 1, 4]
        self.expected_output = 2

    def test_example3(self):
        self.input = [2, 7, 2, 9, 8]
        self.expected_output = 2

    def test_example4(self):
        self.input = [7, 3, 1, 1, 4, 5, 4, 9]
        self.expected_output = 4

    def test_largest_array(self):
        self.input = [1] * 100000
        self.expected_output = 100000

    def test_largest_room(self):
        self.input = [100000] * 100000
        self.expected_output = 1

    def tearDown(self):
        actual = solution(self.input)
        self.assertEqual(self.expected_output, actual)
