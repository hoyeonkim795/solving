from copy import deepcopy
import sys
sys.stdin = open('input.txt','r')

old_board = [[int(x) for x in input().split()] for _ in range(4)]
board = [[(0,0) for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        board[i][j] = (old_board[i][2*j],old_board[i][2*j+1])

# board = (물고기 번호, 물고기의 방향)

dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] #↑, ↖, ←, ↙, ↓, ↘, →, ↗

# 상어는 (0,0) 부터 항상 시작
# 물고기를 먹고 (0,0) 자리에 들어간다 
# 그리고 (0,0)의 물고기의 방향을 갖게된다
shark_position = (0,0)
shark_size,shark_dir = board[0][0]
board[0][0] = ('Shark',shark_size,shark_dir)

# 물고기의 이동!
# 물고기가 이동할 수 있는 경우는 다른 물고기가 있고, 상어가 없을경우
# 이동할 수 있을때까지 반시계 방향으로 45도 회전
def fish_move(board):
    num = 1
    while num < 17:
        flag = 0
        for i in range(4):
            for j in range(4):
                 # 'Shark' 가 아니고 num과 board[i][j][0] 가 찾으려는 물고기 번호와 같을경우 
                if type(board[i][j][0]) == int and board[i][j][0] == num:
                    fish_dir = board[i][j][1]-1
                    while True: # 물고기가 이동할 수 있을 떄 까지 방향 계속 45도 반시계 회전
                        dx,dy = dir[fish_dir]
                        # 상어가 없고 물고기가 있는 자리이며 범위 안에들어올경우 
                        if -1 < i+dx < 4 and -1 < j+dy <4 and board[i+dx][j+dy][0] != 'Shark' and board[i+dx][j+dy] != 0: 
                            board[i][j], board[i+dx][j+dy] = board[i+dx][j+dy],board[i][j]
                            flag = 1
                            break
                        else:
                            fish_dir = (fish_dir + 1)%8
                            board[i][j] = (board[i][j][0],fish_dir+1)
                if flag == 1:
                    break
            if flag == 1:
                break

        num += 1
    return board

board = fish_move(board)
# print(board)
# 물고기가 모두 이동했으니 이제 상어가 이동할 순서이다.
# 상어가 이동 할 수 있는 좌표 후보군들 찾기
stack = []
def shark_stack(stack, shark_size, shark_dir, shark_position, board):
    x, y = shark_position
    for k in range(1,4):
        new_board = deepcopy(board)
        dx,dy = dir[shark_dir-1]
        dx *= k
        dy *= k
        if -1 < x+dx < 4 and -1 < y+dy < 4 and board[x+dx][y+dy][0] != 0: # 범위안에 들어가고 물고기가 있는 자리
            new_shark_size = shark_size + new_board[x+dx][y+dy][0]
            new_shark_dir = new_board[x+dx][y+dy][1]
            new_board[x+dx][y+dy] = ('Shark',new_shark_size,new_shark_dir)
            new_shark_position = (x+dx,y+dy)
            new_board[x][y] = (0,0)
            stack.append([new_shark_size, new_shark_dir, new_shark_position, new_board])
    return stack
stack = shark_stack(stack, shark_size, shark_dir, shark_position, board)
# print(stack)
max_fish_size = 0
while stack:
    shark_size, shark_dir, shark_position, board = stack.pop()
    if shark_size > max_fish_size:
        max_fish_size = shark_size
    # 물고기 이동
    board = fish_move(board)
    stack = shark_stack(stack, shark_size, shark_dir, shark_position, board)

print(max_fish_size)
