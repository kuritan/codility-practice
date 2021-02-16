# A non-empty array A consisting of N integers is given.
# 
# A permutation is a sequence containing each element from 1 to N once, and only once.
# 
# For example, array A such that:
# 
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:
# 
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.
# 
# The goal is to check whether array A is a permutation.
# 
# Write a function:
# 
# def solution(A)
# 
# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
# 
# For example, given array A such that:
# 
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.
# 
# Given array A such that:
# 
#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.
# 
# Write an efficient algorithm for the following assumptions:
# 
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
    """
    :param A: a list of integers
    :return: true if the list is a permutation (sequence from 1 to N)
    """
    # an empty list is not a permutation
    if not len(A):
        return 0

    hits = {}
    for item in A:
        # each element once
        if item in hits:
            return 0
        hits[item] = "HIT"

    # each element once and only once
    if len(hits) != len(A):
        return 0

    # check there is no missing number
    for num in range(1, len(A) + 1):
        if num not in hits:
            return 0

    return 1

if __name__ == '__main__':
    print(solution([5,1,2,3]))