def queue(arr,M):
    for _ in range(M):
        front = arr[0]
        rear = arr[-1]
        new_arr = [0]*N
        new_arr[-1] = front
        for i in range(N-1):
            new_arr[i] = arr[i+1]
        arr = new_arr 
  
    return arr[0]
tc = int(input())
for tc in range(tc):
    N,M = map(int,input().split()) # 숫자개수
    # 작업 횟수
    arr = [0]*N
    info = list(map(int,input().split()))
    for i in range(N):
        arr[i]+=info[i]
    
    print(f'#{tc+1} {queue(arr,M)}')

