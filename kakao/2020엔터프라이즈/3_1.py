import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int,input().split())
snack = []
for i in range(n):
    s = float(input())

    snack.append(s)

h = sum(snack)/k # 일단 예상 값
start, end = 1, max(snack)
a = 1
cnt = 0
while start <= end:
    mid = (start + end) / 2
    cnt = 0
    for i in snack:
        cnt += i// mid
    if cnt >= k:
        start = mid + 0.001
    else:
        end = mid - 0.001

print(format(round(end,2),".2f"))

########## 이거로 답 제출