def clockwise(arr):  # 시계방향으로 k번 만큼 회전
    tmp = arr[0][0]
    arr[0][0] = arr[2][0]
    arr[2][0] = arr[2][2]
    arr[2][2] = arr[0][2]
    arr[0][2] = tmp

    tmp = arr[0][1]
    arr[0][1] = arr[1][0]
    arr[1][0] = arr[2][1]
    arr[2][1] = arr[1][2]
    arr[1][2] = tmp


def U(c):
    if c == '+':
        k = 1
    else:
        k = 3
    for _ in range(k):
        clockwise(cube[0])
        tmp = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
        cube[4][2][0], cube[4][1][0], cube[4][0][0] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
        cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = tmp


def D(c):
    if c == '+':
        k = 1
    else:
        k = 3
    for _ in range(k):
        clockwise(cube[2])
        tmp = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
        cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = tmp


def R(c):
    if c == '+':
        k = 1
    else:
        k = 3
    for _ in range(k):
        clockwise(cube[4])
        tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = tmp


def L(c):
    if c == '+':
        k = 1
    else:
        k = 3
    for _ in range(k):
        clockwise(cube[3])
        tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = tmp


def F(c):
    if c == '+':
        k = 1
    else:
        k = 3
    for _ in range(k):
        clockwise(cube[1])
        tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][0][2], cube[2][0][1], cube[2][0][0]
        cube[2][0][2], cube[2][0][1], cube[2][0][0] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = tmp


def B(c):
    if c == '+':
        k = 1
    else:
        k = 3
    for _ in range(k):
        clockwise(cube[5])
        tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
        cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[2][2][2], cube[2][2][1], cube[2][2][0]
        cube[2][2][2], cube[2][2][1], cube[2][2][0] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = tmp


from copy import deepcopy

CUBE = [[[] for _ in range(3)] for _ in range(6)]

# 큐브 초기화
s = 'wrygbo'  # U F D L R B
for i in range(6):
    for j in range(3):
        for _ in range(3):
            CUBE[i][j].append(s[i])

for _ in range(int(input())):
    n = int(input())
    cmd = input().split()
    cube = deepcopy(CUBE)

    while cmd:
        c = cmd.pop(0)
        if c[0] == 'L':
            L(c[1])
            print(cube)
        elif c[0] == 'D':
            D(c[1])
            print(cube)
        elif c[0] == 'U':
            U(c[1])
            print(cube)
        elif c[0] == 'F':
            F(c[1])
            print(cube)
        elif c[0] == 'R':
            R(c[1])
            print(cube)
        elif c[0] == 'B':
            B(c[1])
            print(cube)

    for i in range(3):
        print(''.join(cube[0][i]))