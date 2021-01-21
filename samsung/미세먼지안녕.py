import sys
sys.stdin = open("input.txt",'r')
r,c,t = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(r)]

# 공기 청정기 위치 찾기
flag = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            machine = [[i,j],[i+1,j]]
            flag = 1
            break
    if flag == 1:
        break

def spread(board):
    new_board = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                temp = 0
                for k in range(4):
                    dx, dy = dir[k]
                    if -1 < i+dx < r and -1 < j+dy < c and board[i+dx][j+dy] != -1:
                        new_board[i+dx][j+dy] += board[i][j]//5
                        temp += 1
                new_board[i][j] += board[i][j]
                new_board[i][j] -= temp*(board[i][j]//5)
            if board[i][j] == -1:
                new_board[i][j] = -1

    return new_board

def move(board):
    up_x, up_y = machine[0]
    down_x, down_y = machine[1]
    new_board = [[0]*c for _ in range(r)]
    # 위에부분

    for j in range(2,c):
        new_board[up_x][j] = board[up_x][j-1]
    new_board[up_x][1] = 0
    for i in range(0,up_x):
        new_board[i][-1] = board[i+1][-1]
        if i != 0:
            for j in range(1,c-1):
                new_board[i][j] = board[i][j]
    for j in range(0,c-1):
        new_board[0][j] = board[0][j+1]
    for i in range(1,up_x):
        new_board[i][0] = board[i-1][0]


    # 아래부분
    for j in range(2,c):
        new_board[down_x][j] = board[down_x][j-1]
    new_board[down_x][1] = 0
    for i in range(down_x+1, r):
        new_board[i][-1] = board[i-1][-1]
    for j in range(c-1):
        new_board[-1][j] = board[-1][j+1]
    for i in range(down_x+1,r-1):
        new_board[i][0] = board[i+1][0]
        for j in range(1,c-1):
            new_board[i][j] = board[i][j]

    # 나머지 채우기
    # for i in range(1,up_x):
    #     for j in range(1,c-1):
    #         new_board[i][j] = board[i][j]
    # for i in range(down_x+1,r-1):
    #     for j in range(1,c-1):
    #         new_board[i][j] = board[i][j]
 
    return new_board

dir = [[1,0],[0,1],[-1,0],[0,-1]]
cnt = 0
for _ in range(t):

    # 미세 먼지의 확산
    
    mid_board = spread(board)

    board = move(mid_board)


ans = 0
print(sum(map(sum, board)))






