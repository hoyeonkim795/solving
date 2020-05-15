
import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('input.txt','r')

q= deque()
n = int(input())
formula = str(input())

op = []

for i in range(len(formula)):
    if formula[i] in ['+','-','*']:
        op.append(formula[i])
n_formula = deepcopy(formula)
new_formula = formula.replace('+','&').replace('*','&').replace('-','&')
number= list(map(int,new_formula.split('&')))
print(number)
for i in range(len(number)-1):
    q.append(i)

def calculate(op,x,y):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y

result = 0

def find(formula,idx):
    global result
    while True:
        if idx >= len(number)-1:
            member = eval(formula)
            formula = deepcopy(n_formula)
            if member > result:
                result = member
            return result
            
        if idx + 1< n:
            formula.replace(formula[idx],'('+formula[idx])
            formula.replace(formula[idx+1],formula[idx+1]+')')
        if idx+2 < n:
            idx+= 2
        find(formula,idx)
        if len(q)!= 0:
            idx = q.popleft()
    return result

idx = q.popleft()
print(find(formula,idx))