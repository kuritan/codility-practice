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

if __name__ == '__main__':
    print(solution(6, [1,6,5,2,2,3,4,5]))