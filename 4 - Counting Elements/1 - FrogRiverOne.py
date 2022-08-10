"""
https://codility.com/media/train/2-CountingElements.pdf
https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
https://app.codility.com/demo/results/trainingG4UY7X-JWB/
"""


def solution(x, a):
    leaf_positions = set()
    for time, leaf_position in enumerate(a):
        if leaf_position <= x:
            leaf_positions.add(leaf_position)
        if len(leaf_positions) == x:
            return time
    return -1
