# 윗면 흰색 아랫면 노란색 앞면 빨간색 뒷면 오렌지색 왼쪽면 초록색 오른쪽 파란색
#U,D,F,B,L,R = w,y,r,o,g,b
def counterclock(order,cube):
    if order == 'U':
        start = cube[2][0]
        cube[2][0] = cube[4][0]
        cube[4][0] = cube[3][0]
        cube[3][0] = cube[5][0]
        cube[5][0] = start
    elif order == 'R':
        start = [cube[0][0][2],cube[0][1][2],cube[0][2][2]]
        for i in range(3):
            cube[0][i][2] = cube[3][i][0]
        for i in range(3):
            cube[3][i][0] = cube[1][i][2]
        for i in range(3):
            cube[1][i][2] = cube[2][i][2]
        for i in range(3):
            cube[2][i][2] = start[i]

    elif order == 'L':

        start = [cube[0][0][0],cube[0][1][0],cube[0][2][0]]
        for i in range(3):
            cube[0][i][0] = cube[2][i][0]
        for i in range(3):
            cube[2][i][0] = cube[1][i][0]
        for i in range(3):
            cube[1][i][0] = cube[3][i][2]
        for i in range(3):
            cube[3][i][2] = start[i]

    elif order == 'D':
        start = cube[2][2]
        cube[2][2] = cube[5][2]
        cube[5][2] = cube[3][2]
        cube[3][2] = cube[4][2]
        cube[4][2] = start

    elif order == 'F':
        start = cube[0][2]
        for i in range(3):
            cube[0][2][i] = cube[5][i][2]
        for i in range(3):
            cube[5][i][2] = cube[1][2][i]
        for i in range(3):
            cube[1][2][i] = cube[4][i][0]
        for i in range(3):
            cube[4][i][0] = start[i]

    elif order == 'B':
        start = cube[0][0]
        for i in range(3):
            cube[0][0][i] = cube[4][i][0]
        for i in range(3):
            cube[4][i][0] = cube[1][0][i]
        for i in range(3):
            cube[1][0][i] = cube[5][i][2]
        for i in range(3):
            cube[5][i][2] = start[i]


#U,D,F,B,L,R = w,y,r,o,g,b
def clock(order,cube):
    if order == 'U':
        start = cube[2][0]
        cube[2][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = cube[4][0]
        cube[4][0] = start
    elif order == 'R':
        start = [cube[0][0][2],cube[0][1][2],cube[0][2][2]]
        for i in range(3):
            cube[0][i][2] = cube[2][i][2]
        for i in range(3):
            cube[2][i][2] = cube[1][i][2]
        for i in range(3):
            cube[1][i][2] = cube[3][i][0]
        for i in range(3):
            cube[3][i][0] = start[i]

    elif order == 'L':
        start = [cube[0][0][0],cube[0][1][0],cube[0][2][0]]
        for i in range(3):
            cube[0][i][0] = cube[3][i][2]
        for i in range(3):
            cube[3][i][2] = cube[1][i][0]
        for i in range(3):
            cube[1][i][0] = cube[2][i][0]
        for i in range(3):
            cube[2][i][0] = start[i]
    elif order == 'D':
        start = cube[2][2]
        cube[2][2] = cube[4][2]
        cube[4][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = start

    elif order == 'F':
        start = cube[0][2]
        for i in range(3):
            cube[0][2][i] = cube[4][i][2]
        for i in range(3):
            cube[4][i][2] = cube[1][2][i]
        for i in range(3):
            cube[1][2][i] = cube[5][i][0]
        for i in range(3):
            cube[5][i][0] = start[i]

    elif order == 'B':
        start =  cube[0][0]
        for i in range(3):
            cube[0][0][i] = cube[5][i][2]
        for i in range(3):
            cube[5][i][2] = cube[1][0][i]
        for i in range(3):
            cube[1][0][i] = cube[4][i][0]
        for i in range(3):
            cube[4][i][0] = start[i]


#U,D,F,B,L,R = w,y,r,o,g,b

tc= int(input())
cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']], [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]]

for tc in range(tc):
    n = int(input())
    info = list(input().split())

    for i in range(len(info)):
        if info[i][1] == '-':
            order = info[i][0]
            counterclock(order,cube)
            print(cube)
        elif info[i][1] == '+':
            order = info[i][0]

            clock(order,cube)
            print(cube)
    # for i in range(3):
    #     print(''.join(cube[0][i]))

