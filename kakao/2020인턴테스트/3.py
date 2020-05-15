#건설 비용을 계산해 보니 
# 직선 도로 하나를 만들 때는 100원이 소요되며, 
# 코너를 하나 만들 때는 500원이 추가로 듭니다

from collections import deque

def calculate(state):

    cnt = 0
    for i in range(1,len(state)-1):
        if state[i] != state[i+1]:

            cnt += 1
    cost= cnt*500 + 100*(len(state)-1)
    return cost
        

def solution(board):
    answer = 0
    dx = (1,0,0,-1)
    dy = (0,1,-1,0)
    #상 우 좌 하
    dstate = (1,0,0,1)
    position = (0,0)
    cost = 0
    n = len(board)
    q = deque()
    q.append((position,'s'))
    visited = [[0 for x in range(len(board[0]))] for _ in range(len(board))]
    result = []
    while q:
        position,state = q.popleft()
        x,y = position
        if position == (n-1,n-1):
            result.append(calculate(state))
        
        if board[x][y] == 0 and visited[x][y] == 0:
            visited[x][y] = 1
            for k in range(4):
                nx,ny = x+dx[k],y+dy[k]
                if -1< nx < len(board) and -1< nx < len(board[0]):
                    if board[nx][ny] == 0:
                        nposition = (nx,ny)
                        nstate = state + str(dstate[k])
                        q.append((nposition,nstate)) 
                        # print(q)

    
    return result





board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))