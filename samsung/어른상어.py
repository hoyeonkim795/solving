import sys
sys.stdin = open("input.txt",'r')
from copy import deepcopy
n, m, K = map(int,input().split())
board = [[int(x) for x in input().split()]for _ in range(n)]
shark_dir = list(map(int,input().split()))
shark = [[[int(x) for x in input().split()] for _ in range(4)] for _ in range(m)]

dir = [(-1,0),(1,0),(0,-1),(0,1)]
