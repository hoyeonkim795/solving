import sys
sys.stdin = open("input.txt",'r')
from copy import deepcopy
board = [[0]*4 for _ in range(4)]
for i in range(4):
    arr = [int(x) for x in input().split()]
    for j in range(4):
        board[i][j] = [arr[j*2],arr[j*2+1]]

dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
eat_num = board[0][0][0]
dead_fish = [board[0][0][0]]
board[0][0][0] = -1
def fish_move(board):
    for num in range(1,17):
        flag = 0
        if num in dead_fish:
            continue
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == num:
                    flag = 1
                    dx, dy = dir[board[i][j][1]-1]
                    nx, ny = i + dx, j + dy
                    if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != [0,0] and board[nx][ny][0] != -1:
                        # nx, ny 가 범위 안에 들어오고 물고기가 있고 상어가 없는 자리라면
                        board[nx][ny], board[i][j] = board[i][j], board[nx][ny]

                    else:
                        k = board[i][j][1]
                        while True:
                            k += 1 
                            k %= 8
                            dx, dy = dir[k-1]
                            nx, ny = i + dx, j + dy
                            if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != [0,0] and board[nx][ny][0] != -1:
                                board[i][j][1] = k
                                board[nx][ny], board[i][j] = board[i][j], board[nx][ny]
                                break
                if flag == 1:
                    break
            if flag == 1:
                break
    return board

board = fish_move(board)
print(board)
def can_eat(a,b,board,eat_num):
    fishes = []
    dx, dy = dir[board[a][b][1]-1]
    for i in range(1,4):
        nx, ny = a+dx*i, b+dy*i
        if -1 < nx < 4 and -1 < ny < 4 and board[nx][ny] != [0,0]:
            fishes.append((a,b,nx,ny,board, eat_num))
    return fishes


stack = can_eat(0,0,board,eat_num)
result = []
while stack:
    a, b, nx, ny, board, eat_num = stack.pop() # 새로운 상어가 위치한자리
    print(a, b, nx, ny, eat_num)
    new_board = deepcopy(board)
    print(new_board)
    # 상어가 새로운 자리에있는 물고기를 먹는다.
    eat_num += board[nx][ny][0]
    result.append(eat_num)
    dead_fish.append(board[nx][ny][0])
    new_board[nx][ny][0] = -1
    # 원래 있던 자리는 물고기 먹어서 사라졌다.
    new_board[a][b] = [0,0]
    # 물고기가 이동한다.
    new_board = fish_move(new_board)
    print(new_board)
    # 새로 이동한 자리에서 먹을 수 있는 물고기의 후보들을 찾는다.
    # print('can eat',can_eat(nx,ny,new_board,eat_num))
    new_stack = can_eat(nx,ny,new_board,eat_num)
    stack += new_stack
    




print(result)

