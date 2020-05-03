import sys
sys.stdin=open('input.txt','r')
n,m=int(input().split())
r,c,d=map(int,input().split()) #북:0 동:1 남:2 서:3
board = [[int(x) for x in input().split()]for _ in range(n)]
visited =[[0 for _ in range(m)]for _ in range(n)]
dir = [[0,-1],[-1,0],[0,1],[1,-0]] # 북동남서
rotate = [3,0,1,2]
while True:
    nx,ny = r+dir[d][0], c+dir[d][1]
    if -1<nx<n and -1<ny<m:
        if visited[nx][ny] == 0 and board[nx][ny] == 0: #왼쪽 방향
            visited[nx][ny] = 1
            r,c = nx,ny
            #1 현재위치 청소부터 진행
        elif visited[nx][ny] == 1:
            d = rotate[d]
            # 2번부터진행
        elif
            
                



