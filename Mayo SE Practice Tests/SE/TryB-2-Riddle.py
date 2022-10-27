# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import unittest


def solution_submitted(riddle):
    # write your code in Python 3.8.10
    listed_riddle = list(riddle)
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

    for index, puzzle in enumerate(listed_riddle):
        if puzzle == '?':
            found = False
            neighbors = get_neighbors(listed_riddle, index)
            for replacement in lowercase_letters:
                if replacement not in neighbors:
                    found = True
                    listed_riddle[index] = replacement
                    break
            if found is False:
                raise Exception

    return ''.join(listed_riddle)


def solution(riddle):   # Improved after submission
    # write your code in Python 3.8.10
    listed_riddle = list(riddle)
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

    for index, puzzle in enumerate(listed_riddle):
        if puzzle != '?':
            continue

        neighbors = get_neighbors(listed_riddle, index)
        for replacement in lowercase_letters:
            if replacement in neighbors:
                continue
            listed_riddle[index] = replacement
            break

    return ''.join(listed_riddle)


def get_neighbors(listed_riddle, index):
    neighbors = set()
    if index-1 >= 0:
        neighbors.add(listed_riddle[index-1])
    if index+1 < len(listed_riddle):
        neighbors.add(listed_riddle[index+1])
    return neighbors


class TestSolution(unittest.TestCase):
    def tearDown(self):
        self.assertIn(self.actual, self.expected)

    def test_example1(self):
        self.expected = {'abcaca', 'abzacd', 'abfacf', 'abcacf'}
        self.actual = solution('ab?ac?')

    def test_example2(self):
        self.expected = {'rdveawgab', 'rdaeawgab'}
        self.actual = solution("rd?e?wg??")

    def test_example3(self):
        self.expected = {'codility', 'abcdefgh', 'abababab'}
        self.actual = solution("????????")

    def test_starts_with_question_has_neighbor(self):
        self.expected = {'codility', 'abcdefgh', 'babababa'}
        self.actual = solution("?a??????")

    def test_riddle_has_more_than_twenty_six_questions(self):
        self.expected = {'ab' * 14}
        self.actual = solution('?' * 28)