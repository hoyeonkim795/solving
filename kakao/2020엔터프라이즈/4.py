from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int,input().split())

now = []
for i in range(m):
    s1,s2,c = input().split()
    now.append([s1,s2,c])

q_num = int(input())

for _ in range(q_num):
    s1,s2 = input().split()
    q = deque()
    q.append([s1,0])
    visited = [0] * len(now)
    result = []
    while q:
        
        ar, cost = q.popleft()

        if ar == s2:
            result.append(cost)

        for i in range(len(now)):
            if now[i][0] == ar and visited[i] == 0:
                q.append([now[i][1],cost + int(now[i][2])])
                visited[i] = 1


    if len(result) >0 :
        print(min(result))
    else:
        print(-1)


    
