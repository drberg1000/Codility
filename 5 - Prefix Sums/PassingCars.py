"""
https://app.codility.com/programmers/lessons/5-prefix_sums/
https://codility.com/media/train/3-PrefixSums.pdf
https://app.codility.com/demo/results/trainingCXWPGS-RKQ/
"""

""" 
Tests: 
(0,1,0,1,0) # 3
(1,0,1,0,1) # 3
(1) # 0
(0) # 0
"""

""" FIRST ATTEMPT """


def solution_1(a):
    passing_car_count=0
    for position, direction_one in enumerate(a, 1):
        if direction_one == 1:
            continue
        for direction_two in a[position:]:
            if direction_one != direction_two:
                passing_car_count += 1
    return passing_car_count


def solution_2(a):
    passing_car_count=0
    for position, direction_one in enumerate(a, 1):
        if direction_one == 1:
            continue

        passing_car_count += sum(a[position:])

    return passing_car_count


def solution(a):
    passing_car_count=0

    prefix_sum = calculate_prefix_sums(a)
    passing_car_count = calculate_passing_car_count(a, prefix_sum)

    return passing_car_count


def calculate_prefix_sums(array):
    prefix_sums = list()
    prefix_sums.append(array[0])
    for element in array[1:]:
        prefix_sums.append(prefix_sums[-1] + element)

    return prefix_sums


def calculate_passing_car_count(array, prefix_sums):
    """ DOH!!! I didn't update this to use prefix_sums! """
    passing_car_count = 0
    for position, direction_one in enumerate(array, 1):
        if direction_one == 1:
            continue

        passing_car_count += sum(array[position:])

    return passing_car_count