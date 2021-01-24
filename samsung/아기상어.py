import sys
sys.stdin = open("input.txt",'r')
from collections import deque
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
queue = deque()

# 상어의 좌표 찾고 queue 만들기
for i in range(n):
    flag = 0
    for j in range(n):
        if board[i][j] == 9:
            queue.append([0,i,j,2,0]) # count , 상어의 x 좌표, 상어의 y좌표, 상어의 크기, 먹은 물고기의 수
            flag = 1
            board[i][j] = 0
            break
    if flag == 1:
        break


dir = [[-1,0],[0,-1],[0,1],[1,0]]
visited = [[0]*n for _ in range(n)]

now = 0 # 단계를 비교하기 위해서
can_eat = [] # 같은 cnt 에서 상어가 먹을 수 있는 물고기의 좌표들
flag = 0 # 상어가 물고기를 먹었을 경유 visited 와 queue 를 초기화 하기 위해 '3번 단계'를 실행하지 않기 위해 존재
ans = 0 # 출력 답

while queue:
    ### 1단계
    cnt, x, y, shark_size, eat_fish_cnt = queue.popleft()

    #### 2단계 (물고기 먹어주기)
    if now < cnt: # 다음단계가 오면 그전에 먹을 수 있는 물고기 후보들 중 조건에 맞는 애를먹는다.

        if len(can_eat) > 0:
            visited = [[0]*n for _ in range(n)] # 방문지 초기화
            can_eat = sorted(can_eat, key = lambda x: (x[0], x[1])) # 가장 위에 있는에 그리고 가장 왼쪽인 애    
            nx, ny = can_eat[0]
            queue = deque() # 물고기를 먹었으니 queue 초기화
            eat_fish_cnt += 1 # 물고기 먹은 개수 늘려주기
            if shark_size == eat_fish_cnt: # 물고기를 먹은 횟수와 상어의 크기가 같다면
                shark_size += 1 # 상어의 크기를 늘려주고
                eat_fish_cnt = 0 # 먹은 횟수는 다시 0 으로 초기화
            board[nx][ny] = 0
            queue.append([cnt,nx,ny,shark_size,eat_fish_cnt])
            can_eat = []
            flag = 1 # queue 를 초기화 하였기 때문에 3번 단계를 실행하지 않고 제일 '1 단계'로 돌아가기 위해
            ans = cnt # 답 갱신

        now = cnt # 현재 단계 갱신

    #### 3단계 (4방향으로 queue 갱신)

    if visited[x][y] == 0 and flag == 0: # 2단계를 수행하지 않았고, 방문하지 않았다면
        visited[x][y] = 1
        for d in range(4): # 4방향으로 검사
            nx, ny = x+dir[d][0], y+dir[d][1]

            if -1 < nx < n and -1 < ny < n and board[nx][ny] <= shark_size and visited[nx][ny] == 0:
                if board[nx][ny] !=0 and board[nx][ny] < shark_size:
                    can_eat.append([nx,ny]) # 먹을 수 있는 물고기 후보들 추가
                queue.append([cnt+1,nx,ny,shark_size,eat_fish_cnt])

    flag = 0 # 2단계 종료후 flag = 1 인 상태인데 다시 queue에 대한 3단계를 실행하기 위해 flag 초기화


print(ans)