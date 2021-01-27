def v(new_board):
    new_board[0][0] = 1
    return 1

board = [[0]*3 for _ in range(3)]
print('1',v(board)) # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print('2',board)   # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

b = 1
def v_1(a):
    a = 3
    return a
print(v_1(b)) # 3
print(b) # 1