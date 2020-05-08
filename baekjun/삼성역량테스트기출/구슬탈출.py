from collections import deque
import sys
sys.stdin = open("input.txt",'r')

n,m = map(int,input().split())
board = [[x for x in input()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            r=i,j
        elif board[i][j] == 'B':
            b=i,j

def move(x,y,dx,dy,ans):
    cnt = 0
    while board[x][y] != '#' and board[x][y] !='O':
        if -1<x+dx<n and -1<y+dy<m:
            cnt += 1
            x +=dx
            y +=dy
    if cnt > 0:
        ans += 1
    return x,y,cnt,ans

rq = deque()
bq = deque()
rq.append(r)
bq.append(b)    
dx = (1,0,-1,0)
dy = (0,1,0,-1)
def bfs():
    ans = 0
    rans,bans = 0,0   
    while ans != 11:
        rx,ry = rq.popleft()
        bx,by = bq.popleft()
        for i in range(4):
            rx,ry,rnt,rans = move(rx,ry,dx[i],dy[i],ans)
            bx,by,bnt,bans = move(bx,by,dx[i],dy[i],ans)
            ans = max(rans,bans)
            if rx == bx and ry == by:
                if rnt > bnt:
                    rx -= dx
                    ry -= dy
                elif rnt < bnt:
                    bx -= dx
                    by -= dy
            if board[rx][ry] == 'O':
                print(ans, "성공")
                ans = 11
                break
                return
            elif board[bx][by] == 'O':
                print(-1,"실패")
                ans = 11
                break
                return
            rq.append((rx,ry))
            bq.append((bx,by))
    if ans == 11:
        print(-1)
        return

bfs()