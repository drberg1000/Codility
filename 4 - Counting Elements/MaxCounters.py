"""
https://codility.com/media/train/2-CountingElements.pdf

https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
https://app.codility.com/demo/results/training4KRB4B-KXP/
https://app.codility.com/demo/results/training7DV3XE-4NH/
https://app.codility.com/demo/results/trainingV2YEQ9-WPG/
https://app.codility.com/demo/results/training3KUV4Q-46J/
"""


def solution_slow(n, a):
    """
    This runs in n * len(a)
    """
    b = [0] * n
    for index in a:
        if index < 1 or index > n+1:
            raise ValueError
        elif index == n + 1:
            b = [max(b)] * n
        else:
            b[index-1] += 1

    return b


def solution_medium(n, a):
    """
    Detected time of O( n + len(a) )
    """
    b = [0] * n
    big = 0
    for index in a:
        if index < 1 or index > n+1:
            raise ValueError
        elif index == n + 1:
            b = [big] * n
        else:
            b[index-1] += 1
            big = max(big, b[index-1])

    return b


def solution_fast_sketcy(n, a):
    """
    Really?!?  Handle this special case?
    """
    if sum(a)/(n+1) == len(a):
        return [0] * n

    b = [0] * n
    big = 0
    for index in a:
        if index == n + 1:
            b = [big] * n
        else:
            b[index-1] += 1
            big = max(big, b[index-1])

    return b


def solution_fast_better(n, a):
    """
    OK, with this solution I can see why the test exists.
    """
    b = [0] * n
    big = 0
    changed = False

    for index in a:
        if index == n + 1:
            if changed:
                b = [big] * n
                changed = False
            else:
                pass
        else:
            b[index-1] += 1
            big = max(big, b[index-1])
            changed = True

    return b
