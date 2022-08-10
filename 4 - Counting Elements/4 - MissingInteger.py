"""
https://codility.com/media/train/2-CountingElements.pdf

https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
https://app.codility.com/demo/results/training9N4MVN-TXF/
https://app.codility.com/demo/results/trainingTG3TDU-325/
https://app.codility.com/demo/results/trainingT5J2D2-HDM/

Make sure your literal numbers match the spec
"""


def solution_wrong_list_size(a):
    # Order the list ignoring duplicates
    b = [None] * 100000
    for element in a:
        if element < 1:
            continue
        b[element] = element

    # Find the smallest missing element
    for index, element in enumerate(b[1:], 1):
        if element is None:
            return index

    return 1


def solution(a):
    # Order the list ignoring duplicates
    b = [None] * 1000001
    for element in a:
        if element < 1:
            continue
        b[element] = element

    # Find the smallest missing element
    for index, element in enumerate(b[1:], 1):
        if element is None:
            return index

    return 1
