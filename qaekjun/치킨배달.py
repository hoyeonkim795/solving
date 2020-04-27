import sys
import math
from itertools import combinations
sys.stdin = open('input.txt','r')
n,m = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]

home = []
store =[]
distance = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home.append([i,j])
        elif board[i][j] == 2:
            store.append([i,j])

def comb(store):
    group = list(combinations(store,m))
    return group


def cal_dis(home,store):
    ans = 2*n*len(home)

    for i in range(len(store)):
        
        mid_ans =0
        for k in range(len(home)):
            smallest = 2*n
            x,y = home[k]
            for j in range(len(store[i])):
                a,b = store[i][j]
                result = abs(x-a)+abs(y-b)
                if result < smallest:
                    smallest = result

            mid_ans += smallest
        if ans>mid_ans:
            ans = mid_ans
    return ans
store = comb(store)
print(cal_dis(home,store))
