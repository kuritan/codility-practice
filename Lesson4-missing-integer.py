def solution(A):
    missing = 1
    
    for num in sorted(A):
        if num == missing:
            missing += 1
        if num > missing:
            break

    return missing