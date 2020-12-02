import sys
from collections import deque
sys.stdin = open("input.txt",'r')

n,m = map(int,input().split())
board = [[x for x in input()]for _ in range(m)]

#움직이는 방향
dir = [(1,0),(0,1),(-1,0),(0,-1)]

# 빨간공과 파란공의 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i,j
        elif board[i][j] == 'B':
            bx, by = i,j

queue = deque()
queue.append([rx,ry,bx,by,1])

visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dir = [(-1,0),(1,0),(0,-1),(0,1)]

def move(x, y, dx, dy):
    count = 0
    if -1< x+dx < n and -1 < y+dy < m: 
        while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
            x += dx
            y += dy
            count += 1
    return x, y, count

def bfs():
    while queue:
        rx,ry,bx,by,depth = queue.popleft()
        if depth > 10:
            break

        for i in range(4):
            nrx, nry, r_count = move(rx,ry,dir[i][0],dir[i][1])
            nbx, nby, b_count = move(bx,by,dir[i][0],dir[i][1])
            
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return depth

                if nrx == nbx and nry == nby:
                    if r_count > b_count:
                        nrx -= dir[i][0]
                        nry -= dir[i][1]
                    elif r_count < b_count:
                        nbx -= dir[i][0]
                        nby -= dir[i][1]
                    

                if visited[nrx][nry][nbx][nby] == False:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append([nrx,nry,nbx,nby,depth+1])
    return -1

print(bfs())
