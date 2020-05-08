import sys
from collections import deque
sys.stdin = open("input.txt",'r')
n,k = map(int,input().split())
visited = [0]*100001
q = deque()
cnt = 0
q.append([n,cnt])


while q:
    x,cnt = q.popleft()
    if visited[x] == 0:
        visited[x] = 1

        if x == k:
            break
        if x-1 >= 0:
            q.append([x-1,cnt+1])
        if x+1 < 100001:
            q.append([x+1,cnt+1])
        if x*2 < 100001:
            q.append([x*2,cnt+1])


print(cnt)

