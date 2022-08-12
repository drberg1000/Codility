"""
https://app.codility.com/programmers/lessons/5-prefix_sums/
https://codility.com/media/train/3-PrefixSums.pdf
https://app.codility.com/demo/results/trainingCXWPGS-RKQ/  # Wasn't sure what's wrong here.  Suspected problems with solution_1() functions.
https://app.codility.com/demo/results/trainingZ2FGJZ-RC6/  # Failed to use the prefix_sums() function.
https://app.codility.com/demo/results/training68T7U2-WCV/  # Realized it should be suffix_sums(). How is this still O(N**2)?
https://app.codility.com/demo/results/trainingWMZTTY-W8K/
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


def solution_3(a):
    passing_car_count=0

    prefix_sum = calculate_prefix_sums_3(a)
    passing_car_count = calculate_passing_car_count_3(a, prefix_sum)

    return passing_car_count


def calculate_prefix_sums_3(array):
    prefix_sums = list()
    prefix_sums.append(array[0])
    for element in array[1:]:
        prefix_sums.append(prefix_sums[-1] + element)

    return prefix_sums


def calculate_passing_car_count_3(array, prefix_sums):
    """ DOH!!! I didn't update this to use prefix_sums! """
    passing_car_count = 0
    for position, direction_one in enumerate(array, 1):
        if direction_one == 1:
            continue

        passing_car_count += sum(array[position:])

    return passing_car_count


""" SECOND ATTEMPT """
" Same as the first, I suspected problems with the extra functions. "


""" THIRD ATTEMPT """

def solution_4(a):
    suffix_sum = calculate_suffix_sums_4(a)
    passing_car_count = calculate_passing_car_count_4(a, suffix_sum)

    return passing_car_count


def calculate_suffix_sums_4(array):
    suffix_sums = []
    suffix_sums.insert(0, array[-1])

    for element in reversed(array[:-1]):
        suffix_sums.insert(0, suffix_sums[0] + element)

    return suffix_sums


def calculate_passing_car_count_4(array, suffix_sums):
    passing_car_count = 0
    for position, direction_one in enumerate(array):
        if direction_one == 1:
            continue
        passing_car_count += suffix_sums[position]

    return passing_car_count


"""" Penultimate """


def solution_5(a):
    suffix_sum = calculate_suffix_sums_5(a)
    passing_car_count = calculate_passing_car_count_5(a, suffix_sum)

    return passing_car_count


def calculate_suffix_sums_5(array):
    suffix_sums = [array[-1]]

    for element in reversed(array[:-1]):
        suffix_sums.append(suffix_sums[0] + element)

    return list(reversed(suffix_sums))


def calculate_passing_car_count_5(array, suffix_sums):
    passing_car_count = 0
    for position, direction_one in enumerate(array):
        if direction_one == 1:
            continue
        passing_car_count += suffix_sums[position]

    return passing_car_count


