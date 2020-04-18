tc = int(input())
for k in range(tc):
    each_count = int(input())
    each_test = list(map(int,input().split()))

    for i in range(len(each_test)-1):
        for j in range(i+1,len(each_test)):
            if each_test[i]> each_test[j]:
                each_test[i],each_test[j] =each_test[j],each_test[i] 
        
    min_test = each_test[0]
    max_test = each_test[-1]
    result = max_test - min_test

    print(f'#{k+1} {result}')