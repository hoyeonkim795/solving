import sys
sys.stdin = open("input.txt",'r')

n, l = map(int,input().split())
board = [[int(x) for x in input().split()]for _ in range(n)]
zip_board = list(map(list,list(zip(*board))))
def solve(board):
    visited = [[0 for _ in range(n)]for _ in range(n)]
    cnt = 0
    for i in range(n):
        flag = 0
        j = 0
        while flag != 1:
            if j >= n-1:
                break
   
            if board[i][j] == board[i][j+1]:
                j += 1
                pass
            elif board[i][j] > board[i][j+1]:
                # 경사로 놓을 수 있는지 검사해야된다.
                for k in range(1,l+1):
                    if j+k < n and board[i][j+k] == board[i][j] - 1 and visited[i][j+k] == 0:
                        pass
                    else:
                        flag = 1
                        break
                if flag == 0:
                    for k in range(1,l+1):
                        visited[i][j+k] = 1
                    j += l 
            elif board[i][j] < board[i][j+1]: #  board[i][j] < board[i][j+1]
                for k in range(l):
                    if j-k >= 0 and board[i][j-k] == board[i][j+1] - 1 and visited[i][j-k] == 0 :
                        pass
                    else:
                        flag = 1
                        break
                if flag == 0:
                    for k in range(l):
                        visited[i][j-k] = 1
                    j += 1
        if flag == 0:
            # print(i)
            cnt += 1
            # print(visited)
    return cnt
# print(solve(board))
# print('----')
# print(solve(zip_board))
print(f'{solve(board) + solve(zip_board)}')