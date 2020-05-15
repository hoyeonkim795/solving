from collections import deque
import sys
sys.stdin = open("input.txt",'r')

# 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳
# 한 칸에서 다른 칸으로 이동하려면, 두 칸이 인접해야 한다. 
# 두 칸이 변을 공유할 때, 인접하다고 한다.

# 벽을 부수고 이동할 수 있는 곳으로 변경한다.
# 그 위치에서 이동할 수 있는 칸의 개수를 세어본다.

n,m = map(int,input().split())
board = [[ int(x) for x in str(input())] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
dx = (1,0,-1,0)
dy = (0,1,0,-1)
