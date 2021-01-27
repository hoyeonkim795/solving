from copy import deepcopy
from itertools import combinations
from collections import deque
import sys
sys.stdin = open("input.txt",'r')
n, m = map(int,input().split())

# 각각의 경우의 수를 다 구한다
def spread(min_cnt, viruses, board_sum, new_board):

    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    cnt = 0
    queue = deque(viruses)
    visited = [[0]*n for _ in range(n)]

    while queue:
        x, y, time  = queue.popleft()

        if time > min_cnt: # 할필요없음
            break
        if board_sum == total:
            return cnt
        for d in range(4):
            nx, ny= dir[d][0] + x, dir[d][1] + y
            if -1 < nx < n and -1 < ny < n and new_board[nx][ny] != 1 :
                if visited[nx][ny] == 0:
                    queue.append([nx,ny,time + 1])
                    if cnt < time+1:
                        cnt = time+1
                    if board[nx][ny] != 2:
                        board_sum += 1
                    visited[nx][ny] = 1

    return -1


board = [[int(x) for x in input().split()] for _ in range(n)]
total = n*n
visited = [[0]*n for _ in range(n)]
# 바이러스가 있는 좌표를 구한다.
virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i,j,0))
            total -= 1
        elif board[i][j] == 1:
            total -= 1

# 바이러스들 중에 M 개를 고른다.
chosens = list(map(list,combinations(virus,m)))
min_cnt = float('inf')
for i in range(len(chosens)):
    chosen = chosens[i]
    new_cnt = spread(min_cnt, chosen, 0, board)

    if new_cnt != -1 and new_cnt < min_cnt:
        min_cnt = new_cnt

    # 바이러스 퍼뜨리기
if min_cnt == float('inf'):
    min_cnt = -1
print(min_cnt)
                        
