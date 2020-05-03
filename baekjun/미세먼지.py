import sys
from collections import deque 
sys.stdin= open('input.txt','r')
r,c,t = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(r)]
#공기청정기 위치와 미세먼지 위치찾기
clean = []
dust = deque()
def pretty(board):
    for i in range(r):
        for j in range(c):
            print(board[i][j],end=' ')
        print()
def find(board):
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                clean.append([i,j])
            elif board[i][j] != 0:
                dust.append([board[i][j],i,j]) #미세먼지양, x좌표, y좌표
    return dust

#먼지 확산
dir = [[0,1],[0,-1],[1,0],[-1,0]]
def spread(dust):
    while dust:
        # print('yes')
        amount,x,y = dust.popleft()
        for i in range(4):
            dx,dy = dir[i][0],dir[i][1]
            nx,ny = x+dx,y+dy
            if -1<nx<r and -1<ny<c:
                if board[nx][ny] == -1:
                    pass
                else:

                    board[nx][ny] += amount//5
                    board[x][y] -= amount//5
    return board

# 공기 청정기 순환 함수 짜야한다 !!!!!!!!!!!

def cnt(board):
    ans = 0
    for i in range(r):
        for j in range(c):
            if board[i][j]!=-1 and board[i][j]!=0:
                ans+=board[i][j]    
    return ans
for _ in range(t):
    dust=find(board)
    board = spread(dust)
    print(pretty(board))
    
    board = purify(board)
    print(board)
print(cnt(board))



# def wind():
#     #상단 x,y
#     x,y = celan[0]
#     end = board[x][-1]
#     for j in range(c-1,1,-1): # ----->
#         board[x][j] = board[x][j-1] 
#     board[x][-1] = end
#     end = board[0][-1]
#     for i in range(x-1):
#         board[i][-1] = board[i+1][-1]
#     board[0][c-2] = end
#     end = board[0][0] 
#     for j in range(c-1):   # <----
#         board[0][j] = board[0][j+1] 
#     board[1][0] = end
#     for i in range(x-1,0,-1):
#         board[i][0] = boad[i-1][0]
    
#     #하단
#     x,y = clean[1]
#     end = board[x][-1]
#     for j in range(c-1,1,-1): # --->
#         board[x][j] = board[x][j-1]

#     board[x+1][-1]=end
#     end=board[r][c] = end
#     for i in range(r-1,x+3,-1):
#         board[i][-1] = board[i-1][-1]

    
    # for j in range(c-1):
    #     board[r][j] = board[r][j+1]
    # board[r][c-2] = end

    