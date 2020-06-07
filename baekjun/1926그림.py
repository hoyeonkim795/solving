import sys
sys.stdin = open("input.txt",'r')

n,m = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(m)]
print(board)