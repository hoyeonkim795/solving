from collections import deque
n= int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer, q = 0,deque()


def get(i,j):
    if board[i][j] !=0:
        q.append(board[i][j])
        board[i][j] = 0

def merge(i,j,di,dj):
    while q:
        x = q.popleft()
        if x == info[i][j]:
            info[i][j] *=2
        elif info[i][j] == 0:
            info[i][j] = x
            i,j = i+di,j+di
        else :
            i,j = i+di,j+di



def move(k):
    if k == 0: #위로 이동
        for j in range(n):
            for i in range(n):
                get(i,j)
            merge(0, j, 1,0) #q 에 값이 다있다 (열)
    elif k == 1: #아래로 이동
        for j in range(n):
            for i in range(n-1,-1,-1):
                get(i,j)
            merge(n-1,j,-1,0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i,j)
            merge(i,0,0,1)
    else:
        for i in range(n):
            for j in range(n-1,-1,-1):
                get(i,j)
            merge(i,n-1,0,-1)

def solve(count):
    global board,answer
    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    b = [x[:] for x in board]

    for k in range(4):
        move(k)
        solve(count+1)
        board = [x[:] for x in b]

solve(0)
print(answer)



