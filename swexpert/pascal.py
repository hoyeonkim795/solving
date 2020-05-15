tc = int(input())
for tc in range(tc):
    n,k = map(int,input().split())
    # 판데기 만들기
    info = [[0 for x in range(n)]for y in range(4)]

    for k in range(1,k+1):
        for i in range(4):
            for j in range(n):
                if info[i][j] == 0:
                    if (i+j+1) % k == 0:
                        info[i][j] = 1
                elif info[i][j] == 1:
                    if (i+j+1) % k == 0:
                        info[i][j] = 0
        print('k가 {}일때'.format(k))
        for i in range(4):
            print(' '.join(map(str,info[i])))
   

    cnt = 0
    for i in range(4):
        for j in range(n):
            if info[i][j] == 1:
                cnt +=1
    print('#{} {}'.format(tc+1, cnt))





