def solution(m, n, puddles):
    answer = 0
    board = [[0]*m for i in range(n)]
    for idx,i in enumerate(puddles):
        i[0] -= 1
        i[1] -= 1
        puddles[idx] = [i[1],i[0]]

    board[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i,j) == (0,0):
                continue
            if [i,j] not in puddles:
                if i == 0 and j!=0:
                    board[i][j] = board[i][j-1]
                elif i!= 0 and j == 0:
                    board[i][j] = board[i-1][j]
                else:
                    board[i][j] = board[i][j-1] + board[i-1][j]
            else:
                board[i][j] = 0
            
    return board[-1][-1]%1000000007