def solution(A):

    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return 1
    else:
        return len(set(A))

