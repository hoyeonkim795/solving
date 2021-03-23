

# 2*2 인 형태일 경우 확인
def check_same(m, n, x, y, friend, board):
    check = [[0,1],[1,0],[1,1]]
    cnt = 0
    for i in range(3):
        dx, dy = check[i]
        if -1 < x+dx < n and -1 < y+dy < m and board[x+dx][y+dy] != 'Zero' and board[x+dx][y+dy] == friend: 
            cnt += 1
        else:
            break
    if cnt == 3:
        return True
    return False

# 없애야 하는 자리
def make_zero(zero_list, board):
    for zero_idx in zero_list:
        x, y = zero_idx
        board[x][y] = 'Zero'
    return board
    

def move(n, m, board):
    for i in range(n):
        for j in range(m-1,-1,-1):
            if board[i][j] == 'Zero':
                nj = j
                cnt = 0
                while nj != -1:
                    if board[i][nj] != 'Zero':
                        board[i] = ['Zero']*cnt + board[i][:nj+1] + board[i][j+1:]
                        break
                    nj -= 1
                    cnt += 1

    return board

def make_list(m, board):
    for i in range(m):
        board[i] = list(board[i])
    return list(map(list,zip(*board)))

def solution(m, n, board):
    answer = 0
    board = make_list(m, board)
    # print(board)
    while True:
        zero_list = []
        flag = 0
        for i in range(n):
            for j in range(m):
                if check_same(m, n, i, j, board[i][j], board):
                    zero_list.append((i,j))
                    zero_list.append((i,j+1))
                    zero_list.append((i+1,j))
                    zero_list.append((i+1,j+1))
                    flag = 1
                    

        if flag == 0:
            # print(board)
            return answer
        else:
            answer += len(set(zero_list))
            board = make_zero(list(set(zero_list)), board)
            board = move(n, m, board)
            # print(board)
        
    return answer


print(solution(4,4,["ABCD", "BACE", "BCDD", "BCDD"]))

[['A', 'B', 'B', 'B'], 
['B', 'A', 'C', 'C'], 
['C', 'C', 'D', 'D'], 
['D', 'E', 'D', 'D']]

[['A', 'B', 'B', 'B'], 
['B', 'A', 'C', 'C'], 
['Zero', 'C', 'C', 'Zero'], 
['Zero', 'D', 'E', 'Zero']]