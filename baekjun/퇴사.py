import sys
sys.stdin = open('input.txt','r')

n = int(input())
t,p = [0]*n,[0]*n

for i in range(n):
    t[i],p[i] = map(int,input().split()) #기간 , 비용
dp = [0]*n
for i in range(n):
    if i+t[i] <= n:
        dp[i] = p[i]
        for j in range(i):
            if (j+t[j]) <= i:
                dp[i] = max(dp[i],dp[j]+p[i])

print(max(dp))
