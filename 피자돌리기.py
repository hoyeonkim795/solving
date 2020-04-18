import copy
def queue(baked,N): #한바퀴 돌리기

    front = baked[0]
    rear = baked[-1]
    new_baked = [0]*N
    new_baked[-1] = front
    for i in range(N-1):
        new_baked[i] = baked[i+1]
    baked = new_baked 

    return baked
def melt(baked):
    baked[0][0] //= 2
    return baked

tc = int(input()) #테스트케이스
for tc in range(tc):
    count = 0
    N,M = map(int,input().split()) #화덕의크기, 피자개수
    C = list(map(int,input().split()))
    new_C = [0]*M
    baked = [None]*N #화덕
    for i in range(M):
        new_C[i] = copy.deepcopy([C[i],i+1]) #인덱스까지 낀 새로운 C만들기
    cnt = 0
    flag = 0
    while flag != 1: #1개 빼고 다 none
        
        if baked[0] == None and cnt != M: #빈 화덕에 피자 넣기 
            baked[0] = copy.deepcopy(new_C[0])
            new_C[0][0] = None #넣은 피자자리는 None
            cnt +=1 # new_C 의 None 의 개수
            # print('화덕에 피자를 넣었다')
            # print(new_C)
            # print(baked)
            new_C = queue(new_C,M) # new_C 돌리기
            baked = queue(baked,N) #baked 돌리기
            
            
        elif  baked[0]!= None and baked[0][0]!= 0 : # 피자가 존재하고 치즈가 있다면
            baked = melt(baked) #피자를 녹이기
            if baked[0][0] == 0: #다 녹은 피자 꺼내기
                baked[0]=None

            else:
                # print('피자를 녹였다',baked)
                baked= queue(baked,N)
                

        elif cnt== M:
            if baked.count(None)==N-1:
                flag = 1 
            baked = queue(baked,N)
    for i in range(N):
        if baked[i] != None:
            print(f'#{tc+1} {baked[i][1]}')
                
