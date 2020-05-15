import copy
R, C, T = map(int, input().split())
info = [[int(x) for x in list(input().split())] for i in range(R)]
new_info = [[0]*C for i in range(R)]
def print_array(array):
    for i in range(len(array)):
        print(' '.join(map(str,array[i])))
def add_array(info,new_info):
    for i in range(len(info)):
        for j in range(len(info[0])):
            info[i][j] += new_info[i][j]
    return info

def push(air, info):
    fl = air[0][0]  # 첫번째 공기청정기의 행
    sl = air[1][0]
    nr = [[0]*len(info[0]) for i in range(len(info))]
    nl = [[0]*len(info[0]) for i in range(len(info))]
    nu = [[0]*len(info[0]) for i in range(len(info))]
    nd = [[0]*len(info[0]) for i in range(len(info))]
    #right
    for j in range(2,len(info[0])):
        nr[fl][j] = info[fl][j-1]
        nr[sl][j] = info[sl][j-1]
    #up
    for i in range(0,fl):
        nu[i][-1] = info[i+1][-1]
    for i in range(sl+1,len(info)-1):
        nu[i][0] = info[i+1][0]
    #left
    for j in range(0,len(info[0])-1):
        nl[0][j] = info[0][j+1]
        nl[-1][j] = info[-1][j+1]
    #down
    for i in range(1,fl-1):
        nd[i][0] = info[i-1][0]
    for i in range(sl+1,len(info)):
        nd[i][-1] = info[i-1][-1]
    #make info 그자리 0
    for j in range(0,len(info[0])):
        info[0][j] = 0 #젤윗줄
        info[-1][j] = 0 #젤아랫줄
    for i in range(0,fl):
        info[i][0] = 0 #윗부분 왼쪽
        info[i][-1] = 0 #윗부분 오른쪽
    info[fl][-1] = 0
    for i in range(sl+1,len(info)):
        info[i][0] = 0 #아래 왼쪽
        info[i][-1] = 0 #아래오른쪽
    info[sl][-1] = 0
    for j in range(1,len(info[0])):
        info[fl][j] = 0 #윗부분 아랫줄
        info[sl][j] = 0 #아랫부분 윗줄

    info = add_array(info,nl)
    info =add_array(info,nu)
    info =add_array(info,nd)
    info =add_array(info,nr)
    return info


def calculate(info):
    result = 0
    for i in range(len(info)):
        for j in range(len(info[0])):
            if info[i][j] != -1:
                result += info[i][j]
    return result



# -1 은 공기청정기 위치
air = []
stack = []
for i in range(R):
    for j in range(C):
        if info[i][j] == -1:
            air.append([i, j])
        elif info[i][j] != 0 and info[i][j] != -1:
            stack.append([i, j])
cnt = 0
while cnt != T :
    #확산시키기
    visited = [[0] * C for i in range(R)]
    while len(stack) > 0:
        x, y = stack.pop()
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        if visited[x][y] != 1:
            visited[x][y] = 1
            num_dir = 0
            for d in range(4):
                dx, dy = dir[d]
                nx, ny = x + dx, y + dy
                if -1 < nx < R and -1 < ny < C and [nx,ny] not in air:
                    new_info[nx][ny] += int((info[x][y])/5)
                    num_dir +=1
            info[x][y] -= int((info[x][y])/5) * num_dir
    info = add_array(info,new_info)
    print('이건 확산')
    print_array(info)
    print('이건 공기청정기')
    info = push(air,info)
    print_array(info)
    cnt += 1
print(calculate(info))
