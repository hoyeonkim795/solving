import sys
from collections import deque
sys.stdin = open('input.txt','r')
T = int(input())
for t in range(T):

    board = [[int(x) for x in input().split()]for _ in range(10)]
    visited = [[0 for _ in range(10)]for _ in range(10)]
    queue = deque()
    total = 0
    dir = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
    for i in range(10):
        for j in range(10):
            if board[i][j] ==1 and visited[i][j] ==0:
                queue.append([i,j])
                total +=1
                while queue:
                    x,y = queue.pop()
                    if board[x][y] == 1 and visited[x][y] ==0:
                        visited[x][y] = 1
                        for d in range(8):
                            dx,dy = dir[d][0],dir[d][1]
                            nx,ny = x+dx,y+dy
                            if -1 <nx < 10 and  -1 <ny < 10:
                                queue.append([nx,ny])
            
    print(f'#{t+1} {total}')



        
