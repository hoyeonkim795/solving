t = int(input())
for tc in range(t):
    V,E = map(int,input().split())
    queue = []
    info =[[0 for _ in range(V+1)]for _ in range(V+1)]
    visited = [0] *(V+1)
    
    for i in range(E):
        x,y = map(int,input().split())
        info[x][y] = 1
        info[y][x] = 1
    S,G =map(int,input().split())
    flag = 0
    queue = []
    queue.append(S)
    
    while queue:
        new_S = queue.pop(0)
        for i in range(V+1):

            if info[new_S][i] == 1 and visited[i]==0:
                
                queue.append(i)
                visited[i] = visited[new_S] + 1
                
                if i == G:
                    flag= 1
        if flag==1:
            print(f'#{tc+1} {visited[G]}')
            break
    if flag == 0:
        print(f'#{tc+1} 0')

    
