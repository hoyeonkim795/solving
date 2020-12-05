import sys
sys.stdin = open("input.txt",'r')
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
dir = [(0,-1),(1,0),(0,1),(-1,0)]
# 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 

##### 흩날리는 모래 비율 (r,c 기준)
# '''''''
# 0 0  2 0 0 
# 0 10 7 1 0
# 5 a  y x 0
# 0 10 7 1 0
# 0 0  2 0 0
# '''''''
def spread_0(r,c,result):
    try:
        board[r-2][c] += board[r][c+1] * 2 // 100
    except IndexError:
        result += board[r][c+1] * 2 // 100
    try:
        board[r-1][c+1] += board[r][c+1] * 1 // 100
    except IndexError:
        result += board[r][c+1] * 1 // 100
    try:
        board[r-1][c] += board[r][c+1] * 7 // 100
    except IndexError:
        result += board[r][c+1] * 7 // 100
    try:
        board[r-1][c-1] += board[r][c+1] * 10 // 100
    except IndexError:
        result += board[r][c+1] * 10 // 100
    try:
        board[r][c-2] += board[r][c+1] * 5 // 100
    except IndexError:
        result += board[r][c+1] * 5 // 100
    try:
        board[r+1][c-1] += board[r][c+1] * 10 // 100
    except IndexError:
        result += board[r][c+1] * 10 // 100
    try:
        board[r+1][c] += board[r][c+1] * 7 // 100
    except IndexError:
        result += board[r][c+1] * 7 // 100
    try:
        board[r+1][c+1] += board[r][c+1] * 1 // 100
    except IndexError:
        result += board[r][c+1] * 1 // 100
    try:
        board[r+2][c] += board[r][c+1] * 2 // 100
    except IndexError:
        result += board[r][c+1] * 2 // 100
    # 남은 모래양
    try:
        board[r][c-1] += board[r][c+1] * 55 // 100
    except IndexError:
        result += board[r][c+1] * 55 // 100

    board[r][c+1] = 0
    return board, result
def spread_1(r,c,result):
    try:
        board[r][c-2] += board[r-1][c] * 2 // 100
    except IndexError:
        result += board[r-1][c] * 2 // 100
    try:
        board[r-1][c-1] += board[r-1][c] * 1 // 100
    except IndexError:
        result += board[r-1][c] * 1 // 100
    try:
        board[r][c-1] += board[r-1][c] * 7 // 100
    except IndexError:
        result += board[r-1][c] * 7 // 100
    try:
        board[r+1][c-1] += board[r-1][c] * 10 // 100
    except IndexError:
        result += board[r-1][c] * 10 // 100
    try:
        board[r+2][c] += board[r-1][c] * 5 // 100
    except IndexError:
        result += board[r-1][c] * 5 // 100
    try:
        board[r+1][c+1] += board[r-1][c] * 10 // 100
    except IndexError:
        result += board[r-1][c] * 10 // 100
    try:
        board[r][c+1] += board[r-1][c] * 7 // 100
    except IndexError:
        result += board[r-1][c] * 7 // 100
    try:
        board[r-1][c+1] += board[r-1][c] * 1 // 100
    except IndexError:
        result += board[r-1][c] * 1 // 100
    try:
        board[r][c+2] += board[r-1][c] * 2 // 100
    except IndexError:
        result += board[r-1][c] * 2 // 100
    # 남은 모래양
    try:
        board[r+1][c] += board[r-1][c] * 55 // 100
    except IndexError:
        result += board[r-1][c] * 55 // 100

    board[r-1][c] = 0
    return board, result
def spread_2(r,c,result):
    try:
        board[r-2][c] += board[r][c-1] * 2 // 100
    except IndexError:
        result += board[r][c-1] * 2 // 100
    try:
        board[r-1][c-1] += board[r][c-1] * 1 // 100
    except IndexError:
        result += board[r][c-1] * 1 // 100
    try:
        board[r+1][c] += board[r][c-1] * 7 // 100
    except IndexError:
        result += board[r][c-1] * 7 // 100
    try:
        board[r-1][c+1] += board[r][c-1] * 10 // 100
    except IndexError:
        result += board[r][c-1] * 10 // 100
    try:
        board[r][c+2] += board[r][c-1] * 5 // 100
    except IndexError:
        result += board[r][c-1] * 5 // 100
    try:
        board[r+1][c+1] += board[r][c-1] * 10 // 100
    except IndexError:
        result += board[r][c-1] * 10 // 100
    try:
        board[r-1][c] += board[r][c-1] * 7 // 100
    except IndexError:
        result += board[r][c-1] * 7 // 100
    try:
        board[r+1][c-1] += board[r][c-1] * 1 // 100
    except IndexError:
        result += board[r][c-1] * 1 // 100
    try:
        board[r+2][c] += board[r][c-1] * 2 // 100
    except IndexError:
        result += board[r][c-1] * 2 // 100
    # 남은 모래양
    try:
        board[r][c+1] += board[r][c-1] * 55 // 100
    except IndexError:
        result += board[r][c-1] * 55 // 100

    board[r][c-1] = 0
    return board, result
def spread_3(r,c,result):
    try:
        board[r][c-2] += board[r+1][c] * 2 // 100
    except IndexError:
        result += board[r+1][c] * 2 // 100
    try:
        board[r+1][c-1] += board[r+1][c] * 1 // 100
    except IndexError:
        result += board[r+1][c] * 1 // 100
    try:
        board[r][c-1] += board[r+1][c] * 7 // 100
    except IndexError:
        result += board[r+1][c] * 7 // 100
    try:
        board[r-1][c-1] += board[r+1][c] * 10 // 100
    except IndexError:
        result += board[r+1][c] * 10 // 100
    try:
        board[r-2][c] += board[r+1][c] * 5 // 100
    except IndexError:
        result += board[r+1][c] * 5 // 100
    try:
        board[r-1][c+1] += board[r+1][c] * 10 // 100
    except IndexError:
        result += board[r+1][c] * 10 // 100
    try:
        board[r][c+1] += board[r+1][c] * 7 // 100
    except IndexError:
        result += board[r+1][c] * 7 // 100
    try:
        board[r+1][c+1] += board[r+1][c] * 1 // 100
    except IndexError:
        result += board[r+1][c] * 1 // 100
    try:
        board[r][c+2] += board[r+1][c] * 2 // 100
    except IndexError:
        result += board[r+1][c] * 2 // 100
    # 남은 모래양
    try:
        board[r-1][c] += board[r+1][c] * 55 // 100
    except IndexError:
        result += board[r+1][c] * 55 // 100

    board[r+1][c] = 0
    return board, result
r,c = n//2,n//2
time = 1
result = 0

while (r,c) != (0,0):
    for d in range(4):
        dx,dy =  dir[d][0],dir[d][1]
        for _ in range(time):
            r, c = r+dx, c+dy
            if d == 0:
                board,result = spread_0(r,c,result)
                print(board,result)
            elif d == 1:
                board,result = spread_1(r,c,result)
                print(board,result)
            elif d == 2:
                board,result = spread_2(r,c,result)
                print(board,result)
            elif d == 3:
                board,result = spread_3(r,c,result)
                print(board,result)
            if (r,c) == (0,0):
                break
        if d == 1 or d == 3:
            time += 1 
        if (r,c)==(0,0):
            break

print(result)


