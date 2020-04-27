#백트래킹 문제
import sys
from collections import deque 
import copy
sys.stdin = open('input.txt','r')
n,m =map(int,input().split())
board =[[int(x) for x in input().split()] for _ in range(n)]

camera = deque()
def pretty(board):
    for i in range(n):
        for j in range(m):
            print(board[i][j],end=' ')
        print()
#카메라 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] !=0 and board[i][j] !=6:
            camera.append([board[i][j],i,j])
    
#사각지대 찾기
def find_0(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt +=1
    return cnt
def camera_num(num):
    if num == 1:
        dir = [[[0,1]],[[1,0]],[[0,-1]],[[-1,0]]]
    elif num == 2:
        dir= [[[0,1],[0,-1]],[[1,0],[-1,0]]]
    elif num == 3:
        dir = [[[-1,0],[0,1]],[[0,1],[1,0]],[[1,0],[0,-1]],[[0,-1],[-1,0]]]
    elif num == 4:
        dir =[[[0,-1],[0,1],[-1,0]],[[-1,0],[0,1],[1,0]],[[0,-1],[0,1],[1,0]],[[0,-1],[-1,0],[1,0]]]
    elif num == 5:
        dir =[[[1,0],[0,1],[-1,0],[0,-1]]]
    return dir

def make(rot,board):
    global result
    if rot == len(camera):
        # print('결과찾아라')
        now = find_0(board)
        if result > now:
            # print('이것은 now',now)
            result = now 
        return 

    num,x,y = camera[rot]
    dir = camera_num(num)
    
    for i in range(len(dir)): #각 case
        p=[]
        # print(num,"카메라",x,y)
        for j in range(len(dir[i])): # 한케이스 내
            nx,ny = x,y
            while True:
                nx+= dir[i] [j][0]
                ny+= dir[i][j][1]
                if -1<nx<n and -1<ny<m:
                    if board[nx][ny] == 6:
                        break
                    else :
                        if board[nx][ny] == 0:
                            board[nx][ny] = '#'
                            p.append([nx,ny])                     
                else:
                    break

        # print(pretty(board))
        # 한케이스르 끝냈으니
        
        make(rot+1,board)
        for i in range(len(p)):
            board[p[i][0]][p[i][1]]=0
            # print("0으로 만들어줌")
            # print(pretty(board))


result = m*n
make(0,board)
print(result)
