def solution(A):
    # write your code in Python 3.6
    A.sort()

    max1 = A[-1] * A[-2] * A[-3]
    max2 = A[0] * A[1] * A[-1]

    if max1 > max2:
        return max1
    else:
        return max2

if __name__ == '__main__':
    print(solution([-3,1,2,-2,5,6]))