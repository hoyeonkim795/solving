def scatter_sand(N, sand_field, r, c, direction):
    ans = 0
    value = sand_field[r][c]
    for i in range(9):
        mr, mc = weight[direction][i]
        nr, nc = r + mr, c + mc
        sand = int((value * percent[i])/100)
        sand_field[r][c] -= sand
        if nr <0 or nc <0 or nr >= N or nc >= N:
            ans += sand
            continue
        sand_field[nr][nc] += sand
    mr, mc = move[direction]
    nr, nc = r + mr, c + mc
    if nr < 0 or nc < 0 or nr >= N or nc >= N:
        ans += sand_field[r][c]
        sand_field[r][c] = 0
    else:
        sand_field[nr][nc] += sand_field[r][c]
        sand_field[r][c] = 0
    return ans




#1:왼쪽, 2: 아래, 3:오른쪽, 4:위
answer = 0
N = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
r, c = N // 2, N // 2

direction = 0
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
distance = 0
weight = [
    [(-1, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-2, 0), (2, 0), (0, -2)],
    [(-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1), (0, -2), (0, 2), (2, 0)],
    [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-2, 0), (2, 0), (0, 2)],
    [(1, -1), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 1), (0, -2), (0, 2), (-2, 0)],
]
percent = [1, 1, 7, 7, 10, 10, 2, 2, 5]


for i in range(N-1):
    distance += 1
    for j in range(2):
        for k in range(distance):
            mr, mc = move[direction]
            r, c = r + mr, c + mc

            answer += scatter_sand(N, board, r, c, direction)
        direction = (direction + 1) % 4
for k in range(distance):
    mr, mc = move[direction]
    r, c = r + mr, c + mc

    answer += scatter_sand(N, board, r, c, direction)

print(answer)