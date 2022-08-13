"""
https://app.codility.com/programmers/lessons/5-prefix_sums/
https://codility.com/media/train/3-PrefixSums.pdf

https://app.codility.com/demo/results/trainingNS2YUM-7T6/

Brutal.  Getting that logic around "extra" right was a trick.
Testing here was way better, but need to find the best way to get the attempts
into codility as I'm going.
"""

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.min_a = 0
        self.max_a = 2000000000

        self.min_k = 1
        self.max_k = 2000000000

    def test_example(self):
        self.a = 6
        self.b = 11
        self.k = 2

        self.expected = 3

    def test_0_2_2(self):
        self.a = 0
        self.b = 2
        self.k = 2

        self.expected = 2

    def test_0_2_4(self):
        self.a = 0
        self.b = 4
        self.k = 2

        self.expected = 3

    def test_0_2_3(self):
        self.a = 0
        self.b = 2
        self.k = 3

        self.expected = 1

    def test_0_3_3(self):
        self.a = 0
        self.b = 3
        self.k = 3

        self.expected = 2

    def test_0_4_3(self):
        self.a = 0
        self.b = 4
        self.k = 3

        self.expected = 2

    def test_1_4_3(self):
        self.a = 1
        self.b = 4
        self.k = 3

        self.expected = 1

    def test_1_4_4(self):
        self.a = 1
        self.b = 4
        self.k = 4

        self.expected = 1

    def test_2_4_4(self):
        self.a = 2
        self.b = 4
        self.k = 4

        self.expected = 1

    def test_3_4_4(self):
        self.a = 3
        self.b = 4
        self.k = 4

        self.expected = 1

    def test_4_4_4(self):
        self.a = 4
        self.b = 4
        self.k = 4

        self.expected = 1

    def test_10_20_2(self):
        self.a = 10
        self.b = 20
        self.k = 2

        self.expected = 6

    def test_10_20_3(self):
        self.a = 10
        self.b = 20
        self.k = 3

        self.expected = 3

    def test_2_4_2(self):
        self.a = 2
        self.b = 4
        self.k = 2

        self.expected = 2

    def test_max_everything(self):
        self.a = self.max_a
        self.b = self.max_a
        self.k = self.max_k

        self.expected = 1

    def test_min_everything(self):
        self.a = self.min_a
        self.b = self.min_a
        self.k = self.min_k

        self.expected = 1

    def test_all_the_things(self):
        self.a = self.min_a
        self.b = self.max_a
        self.k = self.min_k

        self.expected = self.max_a+1

    def tearDown(self):
        actual = solution(self.a, self.b, self.k)
        self.assertEqual(self.expected, actual)


def solution(a, b, k):
    extra = 1
    if a % k == 0:
        extra = 0

    return (b//k+1) - ((a//k) + extra)
