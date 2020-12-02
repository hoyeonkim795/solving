import sys
from itertools import combinations
from itertools import permutations
sys.stdin = open("input.txt",'r')
n = int(input())
board = [[int(x) for x in input().split()]for _ in range(n)]

arr = list(combinations([int(x) for x in range(n)],n//2))

now = 100

for i in range(len(arr)//2):
    # 스타트팀
    sp = list(permutations(arr[i],2))
    lp = list(permutations(arr[-i-1],2))
    start = 0
    link = 0
    for j in range(len(sp)):
        start += board[sp[j][0]][sp[j][1]]
        link += board[lp[j][0]][lp[j][1]]
    
    if now > abs(start-link):
        now = abs(start-link)
print(now)