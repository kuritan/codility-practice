def solution(A):
    # write your code in Python 3.6
    missing_num = 1
    for num in sorted(A):
        if num == missing_num:
            missing_num += 1
        if num > missing_num:
            break
    return missing_num