T = int(input())
for t in range(1, T+1):
    K,N,M = map(int,input().split())
    charger = list(map(int, input().split()))

    start = 0
    end = K
    cnt = 0
    current = 0
    
    while True:
        flag = True
        for i in charger :
            if i > start and i <= end :
                start = i
                flag = False
        if flag :
            cnt = 0
            break

        cnt += 1
        end = start + K

        if end >= N:
            break

    print(f'#{t} {cnt}')