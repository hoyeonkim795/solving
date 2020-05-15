import sys
sys.stdin = open("input.txt","r")

def backtrack(k,result):
    global min_result

    if k == n:
        if min_result > result:
            min_result = result
        return 

    if result > min_result:
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                backtrack(k+1, result+v[k][i])
                visited[i] = 0

t = int(input())
for tc in range(t):
    n= int(input())
    v= [[int(x) for x in input().split()] for _ in range(n)]
    visited = [0]*n
    min_result = 999999999
    backtrack(0,0)
    print(f'#{tc+1} {min_result}')
        
    

