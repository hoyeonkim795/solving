N = int(input())
info = [[int(x) for x in list(input().split())] for _ in range(N)]

#z 0가로 1세로 2대각선
k = 0
def move(x, y,z):
    global k
    if x == N - 1 and y == N - 1:  # 도착시 k + 1
        k += 1
        return


    if z== 0 :  # 가로일때
        if y+1<N and  info[x][y+1] == 0 :
            move(x,y+1,0)
        if y+1<N and x+1<N and  info[x+1][y+1] == 0 and info[x+1][y]==0 and info[x][y+1]==0:
            move(x+1,y+1,2)

    elif z==1 :  # 세로일때
        if x+1<N and  info[x+1][y] == 0 :
            move(x+1,y,1)
        if y+1<N and x+1<N and info[x+1][y+1] == 0 and info[x][y+1]==0 and info[x+1][y]==0:
            move(x+1,y+1,2)

    elif z==2:  # 대각선일떄
        if y+1<N and  info[x][y+1] == 0 :
            move(x,y+1,0)
        if x+1<N and  info[x+1][y] == 0 :
            move(x+1,y,1)
        if y+1<N and x+1<N and info[x+1][y+1] == 0 and info[x][y+1]==0 and info[x+1][y]==0:
            move(x+1,y+1,2)

k=0
move(0,1,0)
print(k)