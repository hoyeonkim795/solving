import sys
sys.stdin = open("input.txt",'r')
from collections import deque
from copy import deepcopy
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]

flag = 0
dir = [[-1,0],[0,-1],[0,1],[1,0]] # 위 왼 오 아래
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            baby = [i,j,2]
            flag = 1
            board[i][j] = 0
            break
    if flag == 1:
        break
flag = 0

def fish(board, baby_size):
    for i in range(n):
        for j in range(n):
            if board[i][j] !=0 and board[i][j] <=baby_size :
                return True
    return False

visited = [[0]*n for _ in range(n)]
baby.append(0)
baby.append(0)
baby.append(visited)

queue = deque()
queue.append(baby)
ans = 0

check = []
now_step = 0
for _ in range(8):
    x, y, baby_size, cnt, time, new_visited = queue.popleft()
    # print(x,y)
    if fish(board,baby_size) == False:
        break
    # print('이것이 cnt', cnt)
    if new_visited[x][y] == 0 and fish(board,baby_size) == True:
        new_visited[x][y] = 1
        for d in range(4):
            dx, dy = dir[d]
            if -1< x+dx < n and -1 < y+dy < n and board[x+dx][y+dy] <= baby_size:
                # 먹을 수 있는 물고기
                if board[x+dx][y+dy] != 0 and board[x+dx][y+dy] < baby_size:
                    check.append([x+dx, y+dy, baby_size, cnt+1, time+1, new_visited])
                else:
                    queue.append([x+dx, y+dy, baby_size, cnt+1, time, new_visited])
        if len(check) > 0:
            if check[0][3] > ans:
                ans = check[0][3]
            queue = deque()
            check[0][5] = [[0]*n for _ in range(n)]
            if check[0][4] == check[0][2]: # time == baby_size 
                check[0][2] += 1
                check[0][4] = 0
            queue.append(check[0])
            board[check[0][0]][check[0][1]] = 0
            # if check[0][3] != check[-1][3]:
            #     check = [len(check)-1]
            # print('---')
            # print(board)


        
print(ans)