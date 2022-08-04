"""
https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
https://app.codility.com/demo/results/trainingQZFA7Z-JN7/
https://app.codility.com/demo/results/trainingBKA5AQ-RPC/
https://app.codility.com/demo/results/training89QZG7-NDE/
https://app.codility.com/demo/results/training4YKH5F-8ZP/
"""

"""
Had problems coming up with the right testcases.  Needed these...
    (-1000, 1000)
    (1,1,3)
    (3,1,1)
...provided to me

What's distinct about the latter two that (3,1,2,4,3) doesn't hit?
"""


def solution_bug_with_two_opposites(a):
    total = sum(a)

    left_part = 0
    lowest_found = total

    for element in a:
        left_part += element
        right_part = total - left_part
        this_difference = abs(left_part - right_part)

        if this_difference < lowest_found:
            lowest_found = this_difference

    return lowest_found


def solution_bug_with_1_1_3(a):
    if len(a) == 2:          # This should have clued me into a problem with the loop.
        return abs(a[0] - a[1])

    total = sum(a)
    left_part = 0            # How could this possibly work without a reference to a[0]
    lowest_found = total

    for element in a[1:-1]:
        left_part += element
        right_part = total - left_part
        this_difference = abs(left_part - right_part)

        if this_difference < lowest_found:
            lowest_found = this_difference

    return lowest_found


def solution_bug_with_3_1_1(a):
    if len(a) == 2:
        return abs(a[0] - a[1])

    total = sum(a)
    left_part = a[0]
    lowest_found = total     # Brain fart here.

    for element in a[1:]:    # Why did I drop the -1?
        left_part += element
        right_part = total - left_part
        this_difference = abs(left_part - right_part)

        if this_difference < lowest_found:
            lowest_found = this_difference

    return lowest_found


def solution(a):
    total = sum(a)

    # Feels like this should absorb into the loop, but how?
    # Input (-1000, 1000) seems to demand it's separate.
    left_part = a[0]
    right_part = total - left_part
    this_difference = abs(left_part - right_part)       # Should have killed this line
    lowest_found = abs(left_part - right_part)

    for element in a[1:-1]:
        left_part += element
        right_part = total - left_part
        this_difference = abs(left_part - right_part)

        if this_difference < lowest_found:
            lowest_found = this_difference

    return lowest_found
