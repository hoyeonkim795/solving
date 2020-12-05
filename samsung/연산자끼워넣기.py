import sys
from itertools import permutations
sys.stdin = open("input.txt",'r')
n = int(input())
A = [int(x) for x in input().split()]
op = [int(x) for x in input().split()]

def calculate(num1,num2,op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    elif op ==  3:
        if num1 < 0:
            return -(abs(num1) // num2)
        else:
            return num1 // num2

op_g = []

for i in range(4):
    if op[i] > 0:
        for _ in range(op[i]):
            op_g.append(i)

op_c = list(set(permutations(op_g,n-1)))


min_result = 100**11 + 1
max_result = -(100**11 + 1)

for i in range(len(op_c)):
    num1 = A[0]
    for j in range(len(op_c[i])):
        num1 = calculate(num1,A[j+1],op_c[i][j])
    if num1 > max_result:
        max_result = num1
    if num1 < min_result:
        min_result = num1
print(max_result)
print(min_result)
        
