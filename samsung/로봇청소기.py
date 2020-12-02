import sys
sys.stdin = open("input.txt",'r')

n, m = map(int,input().split())
# d 가 0 인경우에는 북 쪽 1 인경우에는 동쪽 2인경우에는 남쪽 3인 경우에는 서쪽
r,c,d = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
def find(d):
    if d == 0:
        dx,dy = 0,-1
        nd = 3
    elif d == 1:
        dx,dy = -1,0
        nd = 0
    elif d == 2:
        dx,dy = 0,1
        nd = 1
    elif d == 3:
        dx,dy = 1,0
        nd = 2
    return dx,dy,nd

def back(d):
    if d == 0:
        dx,dy = 1,0
    elif d == 1:
        dx,dy = 0,-1
    elif d == 2:
        dx,dy = -1,0
    elif d == 3:
        dx,dy = 0,1
    return dx,dy

while True:
    # 현재 위치를 청소한다.
    if visited[r][c] == False:
        visited[r][c] = True
        cnt += 1
    # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.

    for _ in range(4):
    # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        dx,dy,nd = find(d)
        if -1 < r + dx < n and -1 < c + dy < m and  board[r+dx][c+dy] != 1 and visited[r+dx][c+dy] == False:
            r,c = r+dx, c+dy
            d = nd
            break
    # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        d = nd
    
    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    else:
        dx,dy = back(d)
        if -1 < r+dx < n and -1 < c+dy < m and board[r+dx][c+dy] == 0:
            r,c = r+dx, c+dy
        # 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
        else:
            break

print(cnt)
