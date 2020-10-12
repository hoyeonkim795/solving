from collections import deque
def correct(s):
    s = deque(s)
    stack = []
    while s:
        a = s.popleft()
        if a == '(':
            stack.append(a)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0 :
        return False
    return True

def reverse(s):
    ans = ''
    for i in s:
        if i == '(':
            ans += ')'
        else:
            ans += '('
    return ans
    
def detatch(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u,v

def solution(p):
    answer = ''
    if p == '' or correct(p):
        return p
    else:
        # 2 u,v 분리
        u,v = detatch(p)
        if correct(u):
            return u + solution(v)
        else:
            # 4단계
            answer += '('
            answer += solution(v)
            answer += ')'
            answer += reverse(u[1:-1])
            return answer

print(solution("()))((()"))