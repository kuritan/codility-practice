def solution(A):
    numset = set()

    for a in A:
        if a in numset:
            numset.remove(a)
        else:
            numset.add(a)

    return numset.pop()

if __name__ == '__main__':
    print(solution([1,2,1,2,3,5,3]))
