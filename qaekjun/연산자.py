import sys
sys.stdin = open('input.txt','r')
from collections import deque
from itertools import permutations
import operator
import math
n=int(input())
a=[int(x) for x in input().split()]
op_info=[int(x) for x in input().split()]
op = deque()
def get_op(op):
    if op == '+' :
        op = operator.add
    elif op =='-' :
        op=operator.sub
    elif op== '*' :
        op = operator.mul
    else:
        op = operator.floordiv
    return op

for _ in range(op_info[0]):
    op.append('+')
for _ in range(op_info[1]):
    op.append('-')
for _ in range(op_info[2]):
    op.append('*')
for _ in range(op_info[3]):
    op.append('/')

combi_op = list(set(permutations(op,len(op))))
ans_max = -(10**9)
ans_min = 10**9

if len(op) == 1:
    ans_min= get_op(combi_op[0][0])(a[0],a[1])
    ans_max= get_op(combi_op[0][0])(a[0],a[1])
else:
    for i in range(len(combi_op)):
        n_result = get_op(combi_op[i][0])(a[0],a[1])
        for j in range(1,len(op)):
            if combi_op[i][j] != '/':
                result = get_op(combi_op[i][j])(n_result,a[j+1])
                n_result = result
            else:
                if n_result < 0:
                    result = get_op(combi_op[i][j])(abs(n_result),a[j+1])
                    result *= -1
                    n_result = result
                else:
                    result = get_op(combi_op[i][j])(n_result,a[j+1])
                    n_result = result


        

        if result >= ans_max:
            ans_max = result
        if result <= ans_min:
            ans_min = result

print(ans_max)
print(ans_min)
    
        



