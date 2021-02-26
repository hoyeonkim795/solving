import sys
sys.stdin = open("input.txt",'r')
n, m, h = map(int,input().split())
board = [[0]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int,input().split())
    board[a-1][b-1] = 1
    board[a-1][b] = -1


# 내려가는거 도착지 찾기
def find_route(board):

    for j in range(n):
        nj = j
        # flag = 0
        # print(j,'찾기')
        for i in range(h):
            if board[i][nj] == 0:
                pass
            elif board[i][nj] == 1 :
                nj += 1

            elif board[i][nj] == -1 :
                nj -= 1

        #     print(i,'행',nj,'열')
        # print('츌발:',j,'도착:',nj)
        if j != nj:
            return False
    return True 

candidate = []
# 가능한 후보 찾기
for i in range(h):
    for j in range(n-1):
        if board[i][j] == 0 and board[i][j+1] ==0 :
            candidate.append([i,j])

# 1개 추가했을때
def add_1():
    for i in range(h):
        for j in range(n-1):
            if board[i][j] == 0 and board[i][j+1] ==0 :
                board[i][j] = 1
                board[i][j+1] = -1
                if find_route(board):
                    return 1
                board[i][j] = 0
                board[i][j+1] = 0
    return -1
# 3개 추가했을떄
def solution():
    for i in range(len(candidate)-1):
        first = candidate[i]
        for j in range(i+1,len(candidate)):
            second = candidate[j]
            if first[0] == second[0]:
                if first[1] + 1 == second[1]:
                    continue 
            board[first[0]][first[1]] = 1
            board[first[0]][first[1]+1] = -1
            board[second[0]][second[1]] = 1
            board[second[0]][second[1]+1] = -1
            if find_route(board):
                return 2
            board[first[0]][first[1]] = 0
            board[first[0]][first[1]+1] = 0
            board[second[0]][second[1]] = 0
            board[second[0]][second[1]+1] = 0    

            if j > len(candidate) - 3:
                continue
            for k in range(j+1,len(candidate)):
                third = candidate[k]
                if second[0] == third[0]:
                    if second[1] + 1 == third[1]:
                        continue
                # print(first,second,third)
                board[first[0]][first[1]] = 1
                board[first[0]][first[1]+1] = -1
                board[second[0]][second[1]] = 1
                board[second[0]][second[1]+1] = -1
                board[third[0]][third[1]] = 1
                board[third[0]][third[1]+1] = -1
                if find_route(board):
                    return 3
                board[first[0]][first[1]] = 0
                board[first[0]][first[1]+1] = 0
                board[second[0]][second[1]] = 0
                board[second[0]][second[1]+1] = 0
                board[third[0]][third[1]] = 0
                board[third[0]][third[1]+1] = 0
    return -1

if find_route(board) or m == 0:
    print(0)
else:
    ans = add_1()
    if ans == -1:
        ans = solution()
        print(ans)
    else:
        print(ans)

