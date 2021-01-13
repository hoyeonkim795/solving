from copy import deepcopy
import sys
from collections import deque
sys.stdin = open("input.txt",'r')
n,q = map(int,input().split())

board = [[int(x) for x in input().split()] for _ in range(2**n)]
l = [int(x) for x in input().split()]

new_board = [[0]*2**n for _ in range(2**n)]

def rotate(key, M):
    new_key = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M-1-i] = key[i][j]
    return new_key

dir = [(0,1),(1,0),(-1,0),(0,-1)]

for k in range(q):
    for i in range(2**n//2**l[k]): #4
            for j in range(2**n//2**l[k]):
                arr = []
                for a in range(2**l[k]):
                    line = []
                    for b in range(2**l[k]):
                        line.append(board[i*2**l[k]+a][j*2**l[k]+b])
                    arr.append(line) 
                new_arr = rotate(arr,2**l[k])
                dir = [(0,1),(1,0),(-1,0),(0,-1)]
                            
                for x in range(2**l[k]):
                    for y in range(2**l[k]):
                        new_board[i*2**l[k]+x][j*2**l[k]+y] = new_arr[x][y]
    

    melt_position=[]
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            for d in range(4):
                    dx,dy = dir[d]
                    if -1 < i+dx < 2**n and -1 < j +dy <2**n and new_board[i+dx][j+dy] != 0:
                        cnt += 1
            if cnt < 3:
                melt_position.append((i,j))

    for m in range(len(melt_position)):
        x,y = melt_position[m]
        if new_board[x][y] > 0:
            new_board[x][y] -= 1

    board = deepcopy(new_board)



result = 0
for i in range(2**n):
    result += sum(new_board[i])

print(result)

# 가장 큰 덩어리 찾기
visited = [[0]*2**n for _ in range(2**n)]

max_size = 0
for i in range(2**n):
    for j in range(2**n):
        size = 0
        if new_board[i][j] != 0 and visited[i][j] == 0:
            stack = [(i,j)]
            while stack:
                x,y = stack.pop()
                if visited[x][y] == 0:
                    size += 1
                    visited[x][y] = 1
                    for d in range(4):
                        dx,dy = dir[d]
                        if -1 < x+dx < 2**n and -1 < y+dy < 2**n and visited[x+dx][y+dy] == 0 and new_board[x+dx][y+dy] != 0:
                            stack.append((x+dx,y+dy))
        if max_size < size:
            max_size = size



print(max_size)
