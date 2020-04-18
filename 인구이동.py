N,L,R = map(int,input().split())
info =[[int(x) for x in input().split()] + [0] for y in range(N) ]
info +=[[0]*(N+1)]
#print(info)
dir = [[0,1],[1,0]]
open_n = 0
cnt = 0
move = 0
end = 1
dif =[]
while True:
    for i in range(0,N):
        for j in range(0,N):
                for k in range(len(dir)):
                #4방향으로 검사
                    dir_x = dir[k][0]
                    dir_y = dir[k][1]
                    nx =dir_x + i
                    ny =dir_y + j
                    if info[nx][ny] !=0:
                        print(info[nx][ny])
                        dif += [abs(info[i][j] - info[nx][ny])]
    #print(dif)
    print(dif)
    for k in range(len(dif)):
        if dif[k] > R or dif[k]<L:
            print(dif[k])
            cnt +=1
    print('이건 cnt',cnt)
        
    if cnt == len(dif):
        break
        
            
                        

    change_idx = []
    for i in range(0,N):
        for j in range(0,N):
            

            for k in range(len(dir)):
                #4방향으로 검사
                dir_x = dir[k][0]
                dir_y = dir[k][1]
                nx =dir_x + i
                ny =dir_y + j
                #print(i,j,nx,ny)
                if info[nx][ny] != 0 and L <= abs(info[i][j] - info[nx][ny]) <= R:
                    change_idx += [[i,j]]
                    change_idx +=[[nx,ny]]
                    flag = 1
                

                    
    
    sum_s = 0         
    s =list(set([tuple(i) for i in change_idx]))
    if len(s)>0:
        for i in range(len(s)):          #평균값 넣기
            
            sum_s += info[s[i][0]][s[i][1]]
        avg = sum_s//len(s)
        for i in range(len(s)):
            info[s[i][0]][s[i][1]] = avg
        print(info)
        move+=1 

    
        
    #print(info)

print(move)


