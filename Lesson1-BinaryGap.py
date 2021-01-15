def solution(N):
    binary_num = format(N, 'b')

    count_zero = 0
    max_zero = 0
    for i in binary_num:
        if i == "1":
            if (count_zero > max_zero):
                max_zero = count_zero
            count_zero = 0
        else:
            count_zero += 1
    return max_zero

if __name__ == '__main__':
    print(solution(1041))