from collections import deque
import sys
sys.stdin = open("input.txt",'r')
n,k = map(int,input().split())
visited = [0]*100001
q = deque()
cnt = 0
q.append([n,cnt])
path = [0]*100001

while q:
    x,cnt= q.popleft()

    if x == k:
        break

    if x+1 < 100001 and visited[x+1] == 0:
        visited[x+1] = 1
        q.append([x+1,cnt+1])
        path[x+1] = x
    if x-1 >= 0 and visited[x-1] == 0:
        visited[x-1] = 1
        q.append([x-1,cnt+1])
        path[x-1] = x
    if x*2 < 100001 and visited[x*2] == 0:
        visited[x*2] = 1
        q.append([2*x,cnt+1])
        path[2*x] = x

result = [x]
print(cnt)
for _ in range(cnt):
    x = path[result[-1]]
    result.append(x)
result.reverse()
for i in range(len(result)):
    print(result[i],end=' ')