def solution(S):
    nested = {'(':1, ')':-1, '{':2, '}':-2, '[':3, ']':-3}
    stack = []

    for s in S:
        if nested[s] > 0:
            stack.append(s)
        else:
            if len(stack)==0:
                return 0
            out = stack.pop()
            if abs(nested[out]) != abs(nested[s]):
                return 0
    if len(stack) != 0:
        return 0
    return 1