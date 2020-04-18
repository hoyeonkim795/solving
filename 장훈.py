tc = int(input())

def backtrack(a,k,input,B):
    final = []
    if k == input:
        result = []
        mid_result = []
        for i in range(input):
            if a[i]:
                mid_result.append(info[i])
        result.append(mid_result)
        sum = 0

        for i in range(len(result)):
            for j in range(len(result[i])):
                sum +=result[i][j]

        if sum > B:
            final.append(sum-B)


    else:
        a[k] = 1
        backtrack(a,k+1,input,B)
        a[k]=0
        backtrack(a,k+1,input,B)




for tc in range(tc):
    N,B =map(int,input().split())
    info = list(map(int,input().split()))
    a = [0] * len(info)
    print(backtrack(a,0,len(info),B))

    #print(f'#{tc+1} {ans}')
