from collections import deque
import sys
import timeit
sys.stdin= open("input.txt",'r')
n, m, k = map(int, input().split())  # 땅의 크기, 나무의 개수, K년이 지난후 상도의 땅

board = [[5] * n for _ in range(n)]

info = [[int(x) for x in input().split()] for _ in range(n)]  # 각 칸에 추가되는 양분의 양
trees = []
for _ in range(m):
    x0, x1, x2 = map(int, input().split())
    trees.append([x2, x0, x1])
# trees = [tuple(int(x) for x in input().split()) for _ in range(m)]  # 나무의 위치, 나무의 나이
trees.sort()

check = [[0] * n for _ in range(n)]
new_trees = [[0]*n for _ in range(n)]
for _ in range(k):
    queue = deque(trees)
    trees = deque()
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, 1], [1, -1], [1, 1], [-1, -1]]
    alive = deque()
    for i in range(n):
        for j in range(n):
            if trees[i][j] > 
        age, x, y = queue.popleft()
        if board[x - 1][y - 1] - age >= 0:
            board[x - 1][y - 1] -= age
            trees.append([age + 1, x, y])
            if (age + 1) % 5 == 0:
                new_trees[x-1][y-1] += 1

        else:  # 양분이 모지랄때
            check[x - 1][y - 1] += age // 2


    for i in range(n):
        for j in range(n):
            board[i][j] += info[i][j] + check[i][j]
            check[i][j] = 0
            if new_trees[i][j] > 0:
                for d in range(8):
                    dx, dy = dirs[d]
                    if -1 < i + dx < n and -1 < j + dy < n:
                        for _ in range(new_trees[i][j]):
                            trees.appendleft([1, i + dx+1, j + dy+1])
            new_trees[i][j] = 0

print(len(trees))