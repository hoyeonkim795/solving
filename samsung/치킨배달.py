from itertools import combinations
import sys
sys.stdin = open("input.txt",'r')
n, m = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]
house = []
store = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            house.append([i,j])
        elif board[i][j] == 2:
            store.append([i,j])
store_c = list(combinations([int(x) for x in range(len(store))],m))

def solve(home_x,home_y,i):
    now = n*2
    for j in range(len(store_c[i])):
        if now > abs(home_x-store[store_c[i][j]][0]) + abs(home_y-store[store_c[i][j]][1]):
            now = abs(home_x-store[store_c[i][j]][0]) + abs(home_y-store[store_c[i][j]][1])
    return now

ans = 9999999999999999999999999999999999999999999999999999999
for k in range(len(store_c)):
    result = 0
    for i in range(len(house)):
        home_x, home_y = house[i]
        result += solve(home_x, home_y,k)
    if ans > result:
        ans = result

print(ans)
