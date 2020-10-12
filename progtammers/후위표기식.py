arr='A*(B+C)'

def solution(arr):
    stack = []
    priority = {
        '*':2,
        '/':2,
        '+':1,
        '-':1,
        '(':0
    }
    for i in '('+arr+')':
        if 'A' <= i <= 'Z':
            print(i,end='')
        elif i == '(':
            stack.append(i)
        elif i== ')':
            while True:
                v = stack.pop()
                if v == '(':
                    break
                print(v,end='')
        else:
            while stack[-1] !='(' and priority[i] <= priority[stack[-1]]:
                print(stack.pop(),end='')
            stack.append(i)
print(solution(arr))