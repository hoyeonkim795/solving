import sys
sys.stdin=open('input.txt','r')
from collections import deque
r,c = map(int,input().split())
board = [[str(x) for x in input()] for _ in range(r)]
water =deque()
stone = deque()
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            mouse = [i,j] #고슴도치 시작위치
        elif board[i][j] == 'D':
            cave = [i,j] #동굴주소
        elif board[i][j] == '*':
            water.append([i,j]) #물의 위치
        elif board[i][j] == 'X':
            stone.append([i,j]) #돌의위치
def pretty(x):
    for i in range(r):
        for j in range(c):
            print(x[i][j],end=' ')
        print()

def flood(i,j):
    queue = deque()
    queue.append([i,j])
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    print(i,j)
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx,ny = x+dir[i][0],y+dir[i][1]
            if -1<nx<r and -1<ny<c:
                if board[nx][ny] == '.':
                    board[nx][ny]='*'
                    queue.append([nx,ny])
            print(queue)

        print(pretty(board))
flood(water[0][0],water[0][1])



