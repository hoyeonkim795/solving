n,l =map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]
zip_board = list(map(list,list(zip(*board))))
# print(zip_board)

def solve(board):
    visited = [[0]*n for _ in range(n)]
    result = 0
    for i in range(n):
        ans = 0
        flag = 0
        j = 0
        while flag != 1:
            if j==n-1:
                flag =1
                continue
            if board[i][j] == board[i][j+1]: #같은 경사
                ans +=1
                j+=1
                # print(f'{i,j} 같은경사')
        
            elif board[i][j] == board[i][j+1]+ 1: # 더높으면
                cnt = 0
                for k in range(l): #경사로를 놓을수있는지 검사
                    if j+1+k <n:
                        if board[i][j+1+k] +1 == board[i][j]:
                            if visited[i][j+1+k]== 0:
                                visited[i][j+1+k] =1
                                cnt +=1
                if cnt == l:
                    ans += l
                    j+=l #l만큼 검사했으니까 뛰어넘기
                    # print(f'{i,j} 내려가는경사')
                else: # 조건만족못하면 다음 행
                    flag =1
                    # print('내려가는 경사 실패군')
            elif board[i][j] == board[i][j+1] -1: # 한칸낮으면
                cnt = 0
                for k in range(l):
                    if j-k > -1:
                        if board[i][j-k] == board[i][j+1] -1:
                            if visited[i][j-k] == 0:
                                visited[i][j-k] =1
                                cnt +=1
                            # else:
                            #     print('이미방문처리가!')

                if cnt == l:
                    ans +=1
                    j+=1
                    # print(f'{i,j} 올라가는경사')
                else:
                    flag = 1
                    # print('올라가는 경사짓기 실패군')

            
            else: #못지나가는경우
                flag = 1
                # print('지나갈수없군')
            if ans == n-1:
                result += 1 #지나갈수있는 경로 +1
    return result

print(f'{solve(board) + solve(zip_board)}')