def solution(A):
    B = {}
    for i in A:
        if i not in B.keys():
            B[i] = 1
        else:
            B[i] += 1
    return len(B.keys())

print(solution([2,1,1,2,3,1]))