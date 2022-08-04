# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# 1st Try https://app.codility.com/demo/results/training252YSM-UTV/ 50%
# 2nd Try https://app.codility.com/demo/results/trainingDBGBF4-6DT/ 100%
# 3rd Try https://app.codility.com/demo/results/trainingMDKY7Y-EWK/ 100%
import math


def solution_incorrect(a):
    """"
    This solution uses O(log n) time to find the missing element once sorted
    Or, it would if it finished.  But this implemenation is incorrect
    """
    b = sorted(a)

    left = 0
    right = len(b)-1
    while True:
        # Find the middle of the portion of interest
        index = math.floor((right-left+1)/2 + left)

        if b[index] == index+1:
            # Everything matches to the index.
            # Throw out the left half.
            left = index
        else:
            # The missing element is on the left or at the index
            if index == 0 or b[index-1] == index:
                # Do things match to the left of the index?
                return index+1
            else:
                # Throw out the right half, including this index
                right = index-1


def solution_sort_binary_search(a):
    """
    This solution uses O(log n) time to find the missing element once sorted

    After looking at other solutions I see that...
    Using binary search over linear search through the sorted array changes
    the complexity from O(2N) to O(N+log(N)).  Not a sufficient savings to
    justify the complexity.
    """
    if len(a) == 0:
        return 1

    b = sorted(a)

    left = 0
    length = right = len(b) - 1

    found = 0
    while not found:
        # Find the middle of the portion of interest
        index = math.floor((right-left+1)/2 + left)
        if b[index] == index+1:
            # Everything matches to the index.
            if index == length:
                # We're at the end, it's the last one that's missing.
                found = index + 2
            else:
                # Throw out the left half including the index
                left = index + 1
        else:
            # The missing element is on the left or at the index
            if index == 0 or b[index-1] == index :
                # Are we already at the beginning?
                # Do things match to the left of the index?
                found = index + 1
            else:
                # Throw out the right half, including this index
                right = index - 1

    return found


def solution_maths(a):
    """
    This implementation doesn't need sorting or search
    Just O(N) time to total up the array.

    More elegant, but the sort/search solution above is still fast enough to
    pass all the requirements and might be easier to understand?  I suppose
    both the binary and the math solution are challenging to follow compared to
    follow compared to an O(N^2) sort/search.

    I knew this trick, but had to look up the formula.
    1 +  2  +  3  +...+ n-2 + n-1 + n
    n + n-1 + n-2 +...+  3  +  2  + 1

    n*(n+1)/2

    1 ==> (1 * 2)/2 = 1
    2 ==> (2 * 3)/2 = 3
    3 ==> (3 * 4)/2 = 6
    4 ==> (4 * 5)/2 = 10
    5 ==> (5 * 6)/2 = 15

    Despite knowing the trick, I didn't think to apply it here
    Without support from Google.
    """
    n = len(a) + 1
    expected = int(n*(n+1)/2)

    return expected - sum(a)
