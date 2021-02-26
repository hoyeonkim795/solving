S = '([)()]'

def solution(S):
    stack = []
    for i in S:
        if i == ')' and len(stack) > 0:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == ']' and len(stack) > 0:
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        elif i== '}' and len(stack)>0:
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    else:
        return 0
print(solution(S))