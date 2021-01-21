import sys
sys.stdin = open("input.txt",'r')
n, k = map(int,input().split())
chess = [[int(x) for x in input().split()] for _ in range(n)]
horses = [[int(x) for x in input().split()] for _ in range(k)]
board = [[[] for _ in range(n)] for _ in range(n)]
# 보드 만들기
for i in range(k):
    x,y,d = horses[i]
    board[x-1][y-1] = [i]

dir = [[0,1],[0,-1],[-1,0],[1,0]]

def blue_and_cant(d,num,x,y,board,horses):
    if d % 2 == 0:
        new_d = d-1
    else:
        new_d = d+1

    num_index = board[x-1][y-1].index(num)
    dx, dy = dir[new_d-1]
    nx, ny = x+dx,y+dy

    if 0 < nx < n+1 and 0 < ny < n+1:
        if chess[nx-1][ny-1] == 0: #흰색일때
            board[nx-1][ny-1] += board[x-1][y-1][num_index:]
            board[x-1][y-1] = board[x-1][y-1][:num_index] # 전의 자리 초기화

        elif chess[nx-1][ny-1] == 1: #빨간색일때
            board[nx-1][ny-1] += list(reversed(board[x-1][y-1][num_index:]))
            board[x-1][y-1] = board[x-1][y-1][:num_index] # 전의 자리 초기화
        elif chess[nx-1][ny-1] == 2:
            nx, ny = x,y
    else:
        nx, ny = x, y

    return nx,ny,new_d,board

def make_horse(nx,ny,d,num,horses):
    for i in range(len(board[nx-1][ny-1])): # 말들 자리 새로 갱신
        horses[board[nx-1][ny-1][i]][0], horses[board[nx-1][ny-1][i]][1] = nx, ny
    horses[num][2] = d # 방향 갱신
    return horses

cnt = 1
flag = 0
ans = -1

while True:
    if flag == 1:
        break
    if cnt >= 1000:
        break
    for num in range(k):
        # print(num)
        x,y,d = horses[num]
        dx, dy = dir[d-1]
        nx, ny = x+dx,y+dy
        if 0 < nx < n+1 and 0 < ny < n+1:
            num_index = board[x-1][y-1].index(num)

            if chess[nx-1][ny-1] == 0: #흰색일때
                board[nx-1][ny-1] += board[x-1][y-1][num_index:] #보드 갱신
                horses = make_horse(nx,ny,d,num,horses)
                board[x-1][y-1] = board[x-1][y-1][:num_index] # 전의 자리 초기화
                # print('1')


            elif chess[nx-1][ny-1] == 1: #빨간색일때
                board[nx-1][ny-1] += list(reversed(board[x-1][y-1][num_index:])) # 보드 갱신
                horses = make_horse(nx,ny,d,num,horses)
                board[x-1][y-1] = board[x-1][y-1][:num_index] # 전의 자리 초기화
                # print('2')

            elif chess[nx-1][ny-1] == 2: # 파란색일떄
                nx,ny,d,board = blue_and_cant(d,num,x,y,board,horses) # 보드 갱신
                horses = make_horse(nx,ny,d,num,horses)
                # print('3')

        else: # 격자 안에 안들어올때
            nx,ny,d, board = blue_and_cant(d,num,x,y,board,horses)
            horses = make_horse(nx,ny,d,num,horses)
        #     print('4')

        # print(board)
        # print(horses)
        
        for i in range(n):
            for j in range(n):
                if len(board[i][j]) >= 4:
                    flag = 1
                    ans = cnt
                    break
            if flag == 1:
                break
    cnt += 1

print(ans)
        

