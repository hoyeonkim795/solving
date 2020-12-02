import sys
from collections import deque
sys.stdin = open("input.txt",'r')
board = [deque([int(x) for x in input()]) for _ in range(4)]
k = int(input())
# N 극은 0 S 극은 1
# 2 : 3시, 6: 9시
for _ in range(k):
    num, dir = map(int,input().split())
    check = []
    if num == 1:
        check.append([0,dir])
        if board[0][2] + board[1][6] == 1:
            check.append([1,-dir])
        if [1,-dir] in check and board[1][2] + board[2][6] == 1:
            check.append([2,dir])
        if [2,dir] in check and board[2][2] + board[3][6] == 1:
            check.append([3,-dir])
    elif num == 2:
        check.append([1,dir])
        if board[1][6] + board[0][2] == 1:
            check.append([0,-dir])
        if board[1][2] + board[2][6] == 1:
            check.append([2,-dir])
        if [2,-dir] in check and board[2][2] + board[3][6] == 1:
            check.append([3,dir])
    elif num == 3:
        check.append([2,dir])
        if board[2][2] + board[3][6] == 1:
            check.append([3,-dir])
        if board[2][6] + board[1][2] == 1:
            check.append([1,-dir])
        if [1,-dir] in check and board[1][6] + board[0][2] == 1:
            check.append([0,dir])
    elif num == 4:
        check.append([3,dir])
        if board[3][6] + board[2][2] == 1:
            check.append([2,-dir])
        if [2,-dir] in check and board[2][6] + board[1][2] == 1:
            check.append([1,dir])
        if [1,dir] in check and board[1][6] + board[0][2] == 1:
            check.append([0,-dir])
    for num,dir in check:
        board[num].rotate(dir)


ans = 0
if board[0][0] == 1:
    ans += 1
if board[1][0] == 1:
    ans += 2
if board[2][0] == 1:
    ans += 4
if board[3][0] == 1:
    ans += 8
print(ans)
