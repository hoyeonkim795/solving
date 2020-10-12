import sys
sys.stdin = open('input.txt','r')

def solution(n,arr):
    priority = {
        '*':2,
        '/':2,
        '-':1,
        '+':1
    }
    stack = []
    cnt = 0
    for i in arr:
        if 'A' <= i <= 'Z':
            stack.append(nums[ord(i)-ord('A')])
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '*':
                stack.append(a*b)
            elif i== '-':
                stack.append(a-b)
            elif i=='/':
                stack.append(a/b)
            elif i=='+':
                stack.append(a+b)
    return stack[0]


n = int(input())
arr = input()
nums= [0]*n


for i in range(n):
    num = int(input())
    nums[i] = num

print('%.2f'% solution(n,arr))