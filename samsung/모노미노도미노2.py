import sys
sys.stdin = open("input.txt",'r')
n = int(input())
# 빨간 보드 
red_green = [[0]*4 for _ in range(10)]
# 초록 보드

# 파란 보드
red_blue = [[0]*10 for _ in range(4)]
# print(red)
# print(green)
# print(blue)

# 빨간 + 초록 
# 빨강의 경계선(행) 까지 간다음에.. 끝까지..
# 한칸씩 내려가기 부딪히면 전으로 돌아가는거
# 특별한 행에 위치한지 확인
    # 지우기, 만들기
# 4칸 다 찾는지 확인
    # 지우기 만들기
# 빨간 + 파란 
# 빨강 경계선 (열) 까지 간다음에 .. 끝까지
# 한칸씩 오른쪽으로 부딪히면 전으로 돌아가는거
# 특별한 열에 위치했는지 확인
    # 지우기, 만들기
# 4칸 다 찾는지 확인
    # 지우기 만들기



for _ in range(n):
    t,x,y = map(int,input().split())
    if t == 1: # 세로
        info = [[x,y]]
    elif t == 2: # 가로
        info = [[x,y],[x,y+1]]
    elif t == 3: # 세로
        info = [[x,y],[x+1,y]]
    
    
    if t == 1:
        # 빨강 + 초록
        nx, ny = x,y
        for i in range(1,10-x):
            if red_green[x+i][y] == 0:
                nx, ny = x+i,y
            else:
                nx, ny = x-1+i,y
                break
        red_green[nx][ny] = 1
        # 빨강 + 파랑
        nx, ny = x,y
        for j in range(1,10-y):
            if red_blue[x][y+i] == 0:
                nx, ny = x,y+i
            else:
                nx, ny = x,y-1+i
        red_blue[nx][ny] = 1
    elif t == 2:
        nx, ny = x, y
        a, b = x, y+1
        # 빨강 + 초록
        for i in range(1,10-x):
            if red_green[x+i][y] == 0 and red_green[x+i][y+1] == 0:
                nx, ny = x+i,y
                a, b = x+i, y+1
            else:
                nx, ny = x+i-1,y
                a, b = x+i-1, y+1
                break
        red_green[nx][ny] = 1
        red_green[a][b] = 1
        # 빨강 + 파랑
        nx, ny = x, y
        a, b = x, y+1
        for i in range(1,9-y):
            if red_blue[x][y+i] == 0 and red_blue[x][y+i+1] == 0:
                nx, ny = x, y+i
                a, b = x, y+1+i
            else:
                nx, ny = x, y+i-1
                a, b = x, y+i
                break
        red_blue[nx][ny] = 1
        red_blue[a][b] = 1
# (2, 2), (3, 2)와 (2, 3), (3, 3)
    elif t == 3:
        nx, ny = x+1,y
        for i in range(1,9-x):
            if red_green[x+1+i][y] == 0 and red_green[x+i][y] == 0:
                nx, ny = x+1+i,y
            else:
                nx, ny = x+i,y
                break
        red_green[nx][ny] = 1
        red_green[nx-1][ny] = 1

        nx, ny = x,y
        for j in range(1,10-y):
            if red_blue[x+1][y+i] == 0 and red_blue[x][y+i] == 0:
                nx, ny = x,y+i
            else:
                nx, ny = x,y-1+i
        red_blue[nx][ny] = 1
        red_blue[nx-1][ny] = 1

print(red_blue)
print(red_green)





