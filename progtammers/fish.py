def solution(A,B):
    stack = [[A[0],B[0]]]
    for i in range(1,len(A)):
        if B[i] == 1:
            stack.append([A[i],B[i]])
        elif B[i] == 0:
            if len(stack) > 0 and stack[-1][1] == 1:
                if stack[-1][0] < A[i]:
                    stack.pop()
                    stack.append([A[i],B[i]])
            else:
                stack.append([A[i],B[i]])
    return len(stack)

            
A =[1,1]
B=[0,1]
print(solution(A,B))