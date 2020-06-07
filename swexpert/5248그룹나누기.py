import sys
from collections import deque
sys.stdin = open("input.txt",'r')

t = int(input())
for tc in range(t):
    n,m = map(int,input().split())
    v = list(map(int,input().split()))
    r = []
    for i in range(0,len(v),2):
        nv = (v[i],v[i+1])
        r.append(nv)
    print(r)
