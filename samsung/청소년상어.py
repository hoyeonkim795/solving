import sys
sys.stdin = open("input.txt",'r')
from copy import deepcopy
board = [[0]*4 for _ in range(4)]
for i in range(4):
    arr = [int(x) for x in input().split()]
    for j in range(4):
        board[i][j] = [arr[j*2]-1,arr[j*2+1]-1]

dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

board[0][0][0] = 'Shark'
# 물고기 대 이동
def fish_move(board):
    for num in range(16):
        for i in range(4):
            flag = 0
            for j in range(4):
                if board[i][j][0] == num: # 해당 번호의 물고기를 찾았다
                    flag = 1
                    dx, dy = dir[board[i][j][1]][0], dir[board[i][j][1]][1]
                    nx, ny = i+dx, j+dy
                    if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != 0 and board[nx][ny][0] != 'Shark':
                        # 범위 안에있고 물고기도 있고 상어가 없는 자리라면
                        board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                        break
                    else: #45도로 움직일 수 있을때까지 계속 회전
                        k = board[i][j][1]
                        while True:
                            k += 1
                            k %= 8
                            dx, dy = dir[k][0], dir[k][1]
                            nx, ny = i+dx, j+dy
                            if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != 0 and board[nx][ny][0] != 'Shark':
                                # 범위 안에있고 물고기도 있고 상어가 없는 자리라면
                                print(board[nx][ny][0])
                                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                                break       
                        flag = 1                 

            if flag == 1:
                break
    return board

board = fish_move(board)
# dfs
stack = []
# 상어의 위치
a,b = 0,0
# 상어가 현재의 위치에서 먹을 수 있는 물고기들의 후보
def can_eat(a,b,stack):
    dx, dy = dir[board[a][b][1]][0], dir[board[a][b][1]][0][1]
    for i in range(1,4):
        nx, ny = a+dx*i, b+dy*i
        if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != 0:
            stack.append((nx,ny))
    return stack

# root
stack = can_eat(a,b,stack)

while stack:
    new_board = deepcopy(board)
    nx, ny = stack.pop()
    new_board[nx][ny][0] = 'Shark'
    
