import sys
sys.stdin = open("input.txt",'r')
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
r,c = n//2,n//2

time =1

dir = [(0,-1),(1,0),(0,1),(-1,0)]

sand = [[(0,-2,5),(-1,-1,10),(-1,0,7),(-1,1,1),(-2,0,2),(1,-1,10),(1,0,7),(1,1,1),(2,0,2),(0,-1),(0,1)],
[(1,1,10),(1,-1,10),(2,0,5),(-1,-1,1),(-1,1,1),(0,-2,2),(0,2,2),(0,-1,7),(0,1,7),(1,0),(-1,0)],
[(0,2,5),(-1,0,7),(1,0,7),(-1,1,10),(-1,2,1),(-2,0,2),(1,1,10),(1,2,1),(2,0,2),(0,1),(0,-1,0)],
[(0,-2,2),(0,2,2),(0,-1,7),(0,1,7),(-1,-1,10),(-1,1,10),(-2,0,5),(1,-1,1),(1,1,1),(-1,0),(1,0)]]



def spread(x,y,r,c,dx,dy,m,result,board):
    total = 0
    if -1 < r+dx < n and -1 < c+dy < n: 
        board[r+dx][c+dy] += board[x][y]*m // 100
        total += board[x][y]*m // 100

    else:
        result += board[x][y]*m // 100
        total += board[x][y]*m // 100

    return board, result, total

result = 0
while (r,c) != (0,0):
    for i in range(4):
        for _ in range(time):
            r,c = r+dir[i][0], c+dir[i][1]
            x,y = r+sand[i][10][0],c+sand[i][10][1]
            a,b = r+sand[i][9][0],c+sand[i][9][1]
            sub = 0
            for s in range(9):
                dx,dy,m = sand[i][s][0],sand[i][s][1],sand[i][s][2]
                board, result, total = spread(x,y,r,c,dx,dy,m,result,board)
                sub += total
            if -1< a < n and -1 < b < n:
                board[a][b] += board[x][y] - sub
            else:
                result += board[x][y] - sub
            board[x][y] = 0
            print(r,c)
            print(board)
            print(result)
            if (r,c) == (0,0):
                break 
        if (r,c) == (0,0):
            break
        if i == 1 or i == 3:
            time += 1



print(result)