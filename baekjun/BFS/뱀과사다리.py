from collections import deque
import sys
sys.stdin = open("input.txt",'r')

board = [-1]*101

n,m= map(int,input().split())

#사다리의 정보
for _ in range(n):
    x,y = map(int,input().split())
    board[x] = y

#뱀의 정보
for _ in range(m):
    u,v = map(int,input().split())
    board[u] = v

q = deque()
visited = [0]*101
p = 1 #현재 위치
cnt = 0
q.append([p,cnt]) # 현재 위치, 횟수

while True:
    p,cnt = q.popleft()

    if p == 100:
        print(cnt)
        break

    if visited[p] == 0:
        #방문한적 없으면
        visited[p] = 1
        for i in range(6):
            np = p+i+1
            if np <= 100:
                if board[np] == -1: # 그자리 정보 없으면 주사위를 돌린만큼 이동
                        q.append([np,cnt+1])
                elif board[np] != -1: #그 자리가 정보있으면
                    sp = board[np] # 거기에 적힌 칸으로 이동한다.
                    q.append([sp,cnt+1])
        

        
