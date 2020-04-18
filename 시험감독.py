import sys
sys.stdin=open('input.txt','r')
import math
n=int(input()) # 시험장 개수
a=[int(x) for x in input().split()] # 한시험장에 응시자의 수
b,c=map(int,input().split()) #총감독관 , 부감독관이 감시할 수 있는 수
cnt = 0
for i in range(n):
    if a[i] > 0:
        a[i] -= b
        cnt+=1
        if a[i]>0:
            cnt += math.ceil(a[i]/c)

print(cnt)