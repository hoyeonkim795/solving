
tc = int(input())
for tc in range(tc):
    N = int(input())
    info =[[int(x) for x in list(input())]for _ in range(N)]
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    visited= [[0 for _ in range(N)] for _ in range(N)]
    
    queue = []
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if info[i][j] == 2:
                start = [i,j] #출발점의 좌표

    #미로 찾기 시작
    
    
    queue.append(start) #스택에 첫 방문지 넣기
   
    while queue:
        flag = 0
        x,y = queue.pop(0)
        for i in range(4):
            dir_x = dir[i][0]
            dir_y = dir[i][1]
            nx= x+dir_x
            ny =y+dir_y

            if -1 < nx < N and -1 < ny < N and visited[nx][ny] == 0:
                if info[nx][ny] == 0 :
                    visited[nx][ny]  =visited[x][y] + 1  #깊이 카운트
                    queue.append([nx,ny])

                elif info[nx][ny] == 3:
                    visited[nx][ny]  = visited[x][y]
                    print(f'#{tc+1} {visited[nx][ny]}')
                    flag = 1
        
        if flag == 1:
            break

    if flag == 0:
        print(f'#{tc+1} 0')

            
