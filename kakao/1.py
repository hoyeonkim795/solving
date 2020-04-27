from collections import deque
def test(box,a,ans):
    if len(box)>0 and a == box[-1]:
        box.pop()
        ans +=2
    else:
        box.append(a)
    return (box,ans)
    
def solution(board, moves):
    answer = 0
    moves = deque(moves)
    print(moves)
    box = deque()
    while moves:
        j = moves.popleft()-1
        
        for i in range(len(board)):
            if board[i][j] != 0:
                box,answer = test(box,board[i][j],answer)
                board[i][j] = 0
                break
    return answer



board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	

print(solution(board,moves))