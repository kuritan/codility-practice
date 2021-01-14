def solution(X, A):
    """
    :param X: an integer. the frogs destination
    :param A: non-empty list of integers
    :return: an integer - the earliest time, or -1
    """
    leaves = {}
    for second in range(0, len(A)):
        leaves[A[second]] = "jumped"
        if len(leaves) == X:
            return second
    return -1
