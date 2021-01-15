def solution(A, K):
    if A == []:
        return A

    for _ in range(K):
        temp = A[-1]
        A.pop(-1)
        A.insert(0, temp)

    return A

if __name__ == '__main__':
    print(solution([1,2,3,4], 2))