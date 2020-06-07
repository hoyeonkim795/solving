import sys
from collections import deque
sys.stdin = open("input.txt",'r')

def cal(a,w):
    if w == 0:
        return a+1
    elif w==1:
        return a-1
    elif w==2:
        return a*2
    else:
        return a-10

       

t = int(input())
for tc in range(t):
    n,m = map(int, input().split())
    cnt= 0
    result = n
    q = deque()
    q.append((result,cnt))
    visited =[0]*1000001
    while q:
        result,cnt = q.popleft()
        if result == m:
            print(f'#{tc+1} {cnt}')
            break
        if visited[result] == 0 and 0 < result < 1000001:
            visited[result] = 1
            for i in range(4):
                nresult = cal(result,i)
                if 0< nresult <1000001:
                    q.append((nresult,cnt+1))



