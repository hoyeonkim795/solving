import sys
sys.stdin = open("input.txt",'r')
# m 나무를 심은 개수
# n 땅의 크기
# k 년후
# info 양분의 정보
n,m,k = map(int,input().split())
tree =[[[0] for _ in range(n)]for _ in range(n)]
info = [[int(x) for x in input().split()]for _ in range(n)]
for _ in range(m):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    print(x,y,z)
    if tree[x][y] == [0]:
        tree[x][y] = [z]
    else:
        tree[x][y] = list(tree[x][y])
        tree[x][y].append(z)
        for i in range(len(tree[x][y])):
            mid = list(tree[x][y])
            result = list(sorted(mid))
            tree[x][y] = result
 

print('나무정보')
print(tree)
board = [[5 for _ in range(n)]for _ in range(n)]
for _ in range(k+1):
#봄
    for i in range(n):
        for j in range(n):
            if tree[i][j][0] != 0 and board[i][j] !=0:
                if board[i][j]-tree[i][j][0] > 0:
                    board[i][j] -=tree[i][j][0]
                    tree[i][j][0] = tree[i][j][0]+1
                else: #자기 나이만큼 없으면 죽는다
                    board[i][j] += tree[i][j][0]//2
                    tree[i][j] = [0]
                        

                    
            elif tree[i][j][0] != 0 and board[i][j] == 0:
                for k in range(len(tree[i][j])): #여름 양분없어서 죽고 양분된다
                    board[i][j] += tree[i][j][k]//2
                tree[i][j] = 0
    # 가을
    dir = [[1,0],[0,1],[-1,0],[0,-1],[-1,1],[1,-1],[1,1],[-1,-1]]
    for i in range(n):
        for j in range(n):
            if tree[i][j]!=[0]:
                for k in range(len(tree[i][j])):
                    if tree[i][j][k]%5== 0:
                        for t in range(8):
                            dx,dy = dir[t]
                            nx,ny = i+dx,j+dy
                            if -1<nx<n and -1<ny<n:
                                if tree[nx][ny]== [0]:
                                    print('나무심기')
                                    tree[nx][ny] = [1]
                                else:
                                    print('나무심기')
                                    tree[nx][ny][k].append(1)
    #겨울
    for i in range(n):
        for j in range(n):
            board[i][j] += info[i][j]
    print('한계절')
    print(tree)
                    
            

    

