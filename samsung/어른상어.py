import sys
sys.stdin = open('input.txt','r')
from copy import deepcopy
n, m, k = map(int,input().split())
# 상어의 번호를 담느 격자
board = [[int(x) for x in input().split()] for _ in range(n)]
# 냄새 영역 표시
# [0,-1] 의 의미는 냄새가 0 이고 -1 은 그 냄새 뿌린 상어의 번호가 올자리
smell = [[[0,-1]]*n for _ in range(n)]
# 각 상어의 방향과 우선순위 정보를 담는 ARR
shark_dir = list(map(int,input().split()))
for i in range(m):
    shark_dir[i] = [shark_dir[i]]
    for _ in range(4):
        shark_dir[i].append(list(map(int,input().split())))
# shark_dir = [방향, [우선순위들...] ]
# print(shark_dir)
cnt = 0
dir = [(-1,0),(1,0),(0,-1),(0,1)]
temp = 0
while True:
    if temp == m-1 : # 1개만 남았을 경우 BREAK
        print(cnt)
        break
    if cnt >= 1000:
        print('-1')
        break

    # 현재 상어가 위치한 자리에 냄새를 뿌린다
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                smell[i][j] = [k,board[i][j]]

    new_board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                d, up, down, left, right = shark_dir[board[i][j]-1]
                dir_arr = [up, down, left, right]
                flag = 0
                for p in range(4):
                    dx, dy = dir[dir_arr[d-1][p] - 1]
                    # 인접한 영역에 냄새가 0 인 경우 우선순위를 고려
                    if -1 < i+dx < n and -1 < j+dy < n and smell[i+dx][j+dy] == [0,-1]:
                        # 이동하는 자리에 어떠한 상어도 없을경우
                        if new_board[i+dx][j+dy] == 0:
                            new_board[i+dx][j+dy] = board[i][j]
                            new_board[i][j] = 0
                        # 이동하는 자리에 다른 상어가 있을경우 넘버를 비교해서 작은것을 위치시키고 temp 를 +1 시킨다 하나 격자밖으로 쫓아내지니까
                        else:
                            if new_board[i+dx][j+dy] > board[i][j]:
                                new_board[i+dx][j+dy] = board[i][j]
                            temp += 1
                            new_board[i][j] = 0
                        shark_dir[board[i][j]-1][0] = dir_arr[d-1][p]
                        flag = 1
                        break
                else:
                    # 인접한 영역에 냄새가 0 인 곳이 없을 경우
                    for p in range(4):
                        dx, dy = dir[dir_arr[d-1][p] - 1]
                        # smell[i+dx][j+dy][1]가 자신의 넘버와 같은 경우 즉 자기의 냄새인 영역
                        if -1 < i+dx < n and -1 < j+dy < n and smell[i+dx][j+dy][1] == board[i][j]:
                            new_board[i+dx][j+dy] = board[i][j]
                            new_board[i][j] = 0
                            shark_dir[board[i][j]-1][0] = dir_arr[d-1][p]
                            break

    board = deepcopy(new_board)
    # 그리고 냄새 영역 이동했으니까 하나씩 줄여주기
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] != -1:
                smell[i][j][0] -= 1
                if smell[i][j][0] == 0:
                    smell[i][j] = [0,-1]
                            
    # print(board)
    # print(smell)
    cnt += 1