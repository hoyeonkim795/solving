tc  = int(input())
for tc in range(tc):
    N = int(input())
    info = []
    for N in range(N):
        info.append(list(map(int,input().split())))
    P = int(input())
    bus_num = []
    for P in range(P):
        bus_num.append(int(input()))


    A = [0]*5001
    for i in range(len(info)):
        start = info[i][0]
        end = info[i][1]

        for k in range(start,end+1):
            A[k] += 1

    print(f'#{tc + 1}',end = ' ')
    for P in range(P+1):

        result = A[bus_num[P]]
        print(result,end=' ')
    print()
