from copy import deepcopy
from itertools import product
import sys
sys.stdin = open("input.txt",'r')
n= int(input())
new_board = [[int(x)for x in input().split() ] for _ in range(n)]
# 5번 돌려서 나올 수 있는 경우의 수
ways = list(product([0,1,2,3],repeat=5))
# dir = [위, 아래, 왼쪽, 오른쪽]

def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

def original(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret


# 밀어주는 함수
def push(i, board, w):

    if w == 2 or w == 1:
        for j in range(n-1):
            while True:
                if board[i][j] == 0:
                    if board[i][j+1:] != len(board[i][j+1:])*[0]:
                        board[i][j:] = board[i][j+1:]
                        board[i].append(0)
                    else:
                        break
                else:
                    break

    elif w == 3 or w == 0:
        for j in range(n-1,0,-1):
            while True:
                if board[i][j] == 0:
                    if board[i][:j] != len(board[i][:j])*[0]:
                        board[i][:j+1] = [0] + board[i][:j]


                    else:
                        break
                else:
                    break

    return board

ans = 0
for way in ways:
    board = deepcopy(new_board)
    for w in way:

        # 왼쪽으로 밀때
        if w == 0 or w == 1:
            board = rotated(board)

        # 먼저 밀어주기
        for i in range(n):
            if sum(board[i]) != 0:
                board = push(i,board,w)


        # 합해주기
        if w == 2 or w == 1: # 아래로 밀때 왼쪽으로 밀때
            for i in range(n):
                if sum(board[i]) != 0:
                    for j in range(n-1):
                        if board[i][j] != 0 and board[i][j] == board[i][j+1]:
                            board[i][j] *= 2
                            board[i][j+1] = 0

        else:
            for i in range(n):
                if sum(board[i]) != 0:
                    for j in range(n-1,0,-1):
                        if board[i][j] != 0 and board[i][j] == board[i][j-1]:

                            board[i][j] *= 2
                            board[i][j-1] = 0


        # 합쳐주기 끝나서 다시 밀어주기
        for i in range(n):
            if sum(board[i]) != 0:
                board = push(i,board,w)
            
        # 돌린거는 다시 제자리로
        if w == 0 or w == 1:
            board = original(board)

    for i in range(n):
        if ans < max(board[i]):
            ans = max(board[i])

print(ans)
        