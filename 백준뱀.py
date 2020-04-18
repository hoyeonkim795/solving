import sys
from collections import deque 
sys.stdin = open('snake.txt', 'r')

n = int(input())
k = int(input())

state = 'r' # r,l,u,d 가려는 방향

snake = deque()
board = [[0]*n for _ in range(n)]

for _ in range(k):
    i,j = map(int,input().split())
    board[i-1][j-1] = 1

l = int(input())
info = deque()
for _ in range(l):
    x, c = input().split()
    x = int(x)
    
    info.append([x+1,c])

def rotate(state):
    a,x = info.popleft()

    if x == 'D':
        if state == 'r':
            state = 'd'
        elif state == 'd':
            state = 'l'
        elif state == 'l':
            state = 'u'
        else:
            state = 'r'
    else: #왼쪽
        if state == 'r':
            state = 'u'
        elif state == 'u':
            state = 'l'
        elif state == 'l':
            state = 'd'
        else:
            state = 'r'
    return state

def get(i,j,state):
    if state == 'r':
        i,j = i,j+1

    elif state == 'd':
        i,j = i+1,j
    elif state == 'l':
        i,j = i,j-1
    else:
        i,j = i-1,j
    
    return (i,j)

def move(i,j,state):

    board[i][j] = 2 # 뱀이있는자리
    snake.append([i,j])
    flag = 0
    t=0
    while flag!=1:
        t = t+1
        if len(info)!=0 and t == info[0][0]:
            state = rotate(state)
        i,j = get(i,j,state) #뱀이 바라보는 방향으로 이동 # 다음칸으로 이동한다
        if  -1< i < n and -1< j < n: #첫시작이 00이여서 값이 제대로 안나오는거고
            
            if board[i][j] == 1: #사과가 있다면
                snake.appendleft([i,j])
                board[i][j] =2
                #꼬리는 그대로
                
            elif board[i][j]==0 : #사과가 없다면
                board[i][j] = 2
                snake.appendleft([i,j])
                t_x,t_y = snake.pop()
                board[t_x][t_y] = 0

                #꼬리가 움직인만큼 움직인다.
            elif board[i][j]==2: #뱀의 몸통이라면
                flag = 1
                break
        else:
            flag = 1
            break
    return t

print(move(0,0,state))
