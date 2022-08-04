"""
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
https://app.codility.com/demo/results/training5MQQG9-DYG/
https://app.codility.com/demo/results/training79TSX2-3Z8/
"""


def solution_bug_with_doubles(a):
    """ Didn't read the directions carefully enough and missed a test case"""
    a = set(a)
    if len(a) != max(a):
        return 0
    return 1


def solution(a):
    b = set(a)
    if len(a) != len(b):
        return 0
    if len(b) != max(a):
        return 0
    return 1
