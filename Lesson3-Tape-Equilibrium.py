def solution(A):
    # write your code in Python 3.6
    left = 0
    minimal = None
    right = sum(A)

    for P in range(0, len(A)-1):
        left += A[P]
        right -= A[P]
        diff = abs(left - right)

        if minimal is None or diff < minimal:
            minimal = diff

    return minimal