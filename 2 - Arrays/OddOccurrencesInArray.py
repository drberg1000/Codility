def solution_fast(A):
    unmatched = set()
    while A:
        element = A.pop()
        if element in unmatched:
            unmatched.remove(element)
        else:
            unmatched.add(element)

    return unmatched.pop()


def solution_slow(A):
    for element in A:
        if A.count(element) % 2 == 1:
            return element
