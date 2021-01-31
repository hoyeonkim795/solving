from copy import deepcopy
import sys
sys.stdin = open("input.txt",'r')

R, C, M = map(int,input().split())
board = [[[0,0,0]]*C for _ in range(R)]

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    board[r-1][c-1] = [s,d,z] #속력, 이동방향, 크기

dir = [[-1,0],[1,0],[0,1],[0,-1]]
# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 상어가 이동한다.
ans = 0
print(board)
for j in range(C):
    for i in range(R):

        if board[i][j] != [0,0,0]:
            ans += board[i][j][2]
            board[i][j] = [0,0,0]
            break

    # 상어의 이동
    new_board= [[[0,0,0]]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != [0,0,0]:
                fast = board[i][j][0]
                dx, dy = dir[board[i][j][1]-1]
                dx *= fast
                dy *= fast
                nx, ny = i+dx, j + dy
                if -1 < nx < R and -1 < ny < C:
                    if new_board[nx][ny] == [0,0,0]: # 아무도 없을때
                        new_board[nx][ny] = board[i][j]
                    else: # 있다면 잡아먹으렴...
                        if new_board[nx][ny][2] < board[i][j][2]:
                            new_board[nx][ny] = board[i][j]
                else: #dir = [[-1,0],[1,0],[0,1],[0,-1]]

                    if -1 < nx < R and -1 < ny < C:
                        if new_board[nx][ny] == [0,0,0]: # 아무도 없을때
                            new_board[nx][ny] = board[i][j]
                            new_board[nx][ny][1] = d+1
                        else: # 있다면 잡아먹으렴...
                            if new_board[nx][ny][2] < board[i][j][2]:
                                new_board[nx][ny] = board[i][j]
                                new_board[nx][ny][1] = d+1
    board = deepcopy(new_board)
    print('------')
    print(board)
                        
                        

print(ans)
