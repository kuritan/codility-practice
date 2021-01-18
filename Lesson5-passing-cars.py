def solution(A):
    # write your code in Python 3.6
    east = 0
    pairs = 0

    for i in range(len(A)):
        if A[i] == 0:
            east += 1
        elif A[i] == 1:
            pairs += east
            if pairs > 1000000000:
                return -1    
    return pairs

if __name__ == '__main__':
    print(solution([0,1,0,1,1]))