import sys
sys.stdin = open("input.txt",'r')
n = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]
flag = 0
dir = [[-1,0],[0,-1],[0,1],[1,0]]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            baby = [i,j,2]
            flag = 1
            break
    if flag == 1:
        break
flag = 0
cnt = 0
while True:
    if flag == 1:
        break
    for d in range(4):
        dx, dy = dir[d]
        if -1 < baby[0]+dx < n and -1 < baby[1]+dy < n:
            


