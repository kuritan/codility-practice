def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)
    """
    # an empty list is not a permutation
    if not len(A):
        return 0

    hits = {}
    for item in A:
        # each element once
        if item in hits:
            return 0
        hits[item] = "HIT"

    # each element once and only once
    if len(hits) != len(A):
        return 0

    # check there is no missing number
    for num in range(1, len(A) + 1):
        if num not in hits:
            return 0

    return 1

if __name__ == '__main__':
    print(solution([5,1,2,3]))