n,m = map(int,input().split())
board = [[int(x) for x in input().split()]for _ in range(n)]


dir_1 = [(0,0), (0,1), (0,2), (0,3)] # 직선가로
dir_2 = [(0,0), (1,0), (2,0), (3,0)] #직선세로
dir_3 =[(0,0), (0,1), (1,0), (1,1)] # 사각형
dir_4 = [(0,0), (0,1), (0,2), (1,0)] #ㄴ
dir_5 = [(1,0), (1,1), (1,2), (0,2)] #반대 ㄴ
dir_6 = [(0,0), (1,0), (1,1), (1,2)] # 꺽임
dir_7 = [(0,0), (0,1), (0,2), (1,2)]
dir_8 = [(0,0), (1,0), (2,0), (2,1)] #ㅜ
dir_9 = [(2,0), (2,1), (1,1), (0,1)] # ㅗ
dir_10 =  [(0,0), (0,1), (1,0), (2,0)] #긴 ㄱ 
dir_11= [(0,0), (0,1), (1,1), (2,1)] # 긴 반대 ㄱ
dir_12=[(0,0), (0,1), (0,2), (1,1)]
dir_13=[(1,0), (1,1), (1,2), (0,1)]
dir_14=[(1,0), (0,1), (1,1), (2,1)]
dir_15=[(0,0), (1,0), (2,0), (1,1)]
dir_16=[(1,0), (2,0), (0,1), (1,1)]
dir_17=[(0,0), (1,0), (1,1), (2,1)]
dir_18=[(1,0), (0,1), (1,1), (0,2)]
dir_19=[(0,0), (0,1), (1,1), (1,2)]


def find(dir,x,y):
    total = 0
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        try:
            total += board[nx][ny] 
        except IndexError:
            continue
    return total
        

t_max = 0
for i in range(n):
    for j in range(m):

        now_max = max(find(dir_1,i,j),find(dir_2,i,j),find(dir_3,i,j),find(dir_4,i,j),find(dir_5,i,j),find(dir_6,i,j),find(dir_7,i,j),find(dir_8,i,j),find(dir_9,i,j),find(dir_10,i,j),find(dir_11,i,j),find(dir_12,i,j),find(dir_13,i,j),find(dir_14,i,j),find(dir_15,i,j),find(dir_16,i,j),find(dir_17,i,j),find(dir_18,i,j),find(dir_19,i,j))
        if t_max < now_max:
            t_max=now_max 
print(t_max)