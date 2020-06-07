import sys
sys.stdin = open('input.txt', 'r')
n,k = map(int,input().split())

snack = []
for i in range(n):
    s = float(input())
    snack.append(s)

snack_min = min(snack)
standard = sum(snack)/k

cnt = 0
# while cnt != k:
while int(cnt) != k:
    cnt = 0
    for i in range(len(snack)):
        cnt += (snack[i]//snack_min)
    snack_min -= 0.001


print(format(round(snack_min,2),".2f"))