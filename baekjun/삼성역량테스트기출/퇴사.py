from collections import deque 
import sys
sys.stdin = open('input.txt','r')

q = deque()
n = int(input())
t,p = [0]*(n+1),[0]*(n+1)
money = 0

for i in range(n):
    t[i+1],p[i+1] = map(int,input().split()) #기간 , 비용

# 시작점 다넣기
for i in range(1,n+1):
    if i+t[i] <= n+1:
        q.append((i,p[i]))

while q:
    d,cost = q.popleft()
    if cost > money:
        money = cost
    nds = d+t[d] # 그 다음 시작할 수 있는 상담수
    for x in range(nds,n+1):
        if x+t[x] <=n+1:
            q.append((x,cost+p[x]))

print(money)