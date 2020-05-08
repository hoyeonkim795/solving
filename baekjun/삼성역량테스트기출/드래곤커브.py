from collections import deque
import sys
sys.stdin = open('input.txt','r')
'''
0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
 x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
a,b 기준점 움직이려는 점 x,y
x' = (x-lx) * cos(270) - (y-ly)sin(270) +lx
y' = (x-lx) * sin(270) + (y-ly)cos(270) + ly
'''
visited = [[0 for _ in range(101)]for _ in range(101)]
n= int(input())
info =deque()
for _ in range(n):
    x,y,d,g = map(int,input().split())
    info.append([x,y,d,g])

def square():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if visited[i][j] == 1:
                if i+1<100 and j+1<100:
                    if visited[i+1][j] ==1 and visited[i][j+1] == 1 and visited[i+1][j+1] ==1:
                        cnt +=1 
    return cnt
def check(x,y,d,g):
    now = deque()
    #nx,ny는 0세데 좌표
    if d == 0:
        nx,ny = x+1,y
    elif d==1:
        nx,ny = x,y+1
    elif d==2:
        nx,ny = x-1,y
    elif d==3:
        nx,ny = x,y-1
    visited[x][-y] = 1
    visited[nx][-ny] =1
    now.append([x,y])
    now.append([nx,ny])
    result = deque([[x,y],[nx,ny]])
    for _ in range(g):
        lx,ly = now.pop() #기준점 좌표
        ly = ly
        while now:
            x,y = now.pop()
            nx=y-ly +lx
            ny=-x+lx+ly
            visited[nx][-ny] = 1
            result.append([nx,ny])
        now = deque(result)

    
for i in range(len(info)):
    x,y,d,g = info.popleft()
    y=-y
    check(x,y,d,g)
print(square())



