from collections import deque
import sys
sys.stdin = open("input.txt",'r')
n, m, gas = map(int,input().split())
board = [[int(x) for x in input().split()] for _ in range(n)]
driver = [int(x) for x in input().split()]
people = [[int(x) for x in input().split()] for _ in range(m)] # 행, 열, 도착행, 도착열

# 행번호가 가장 작은 승객, 열 번호가 가장 작은 승객

# BFS

people_cnt = len(people)

# 택시에서 가장 가까운 사람을 고른다.
def find_nearest(driver, people, people_index, flag):
    min_now = float('inf')
    each_distance = []
    shortest = []
    queue = deque()
    arr = driver + [0]
    queue.append(arr)
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = [[0]*n for _ in range(n)]
    stop = 0
    while queue:
        x, y, distance = queue.popleft()
        if flag == 0: # 가장 가까운 사람 찾기
            for p in range(len(people)):
                if (x,y) == (people[p][0],people[p][1]):
                    if distance > min_now:
                        stop = 1
                        break
                    else:
                        min_now = distance
                        each_distance.append([p,x,y,distance])
                        break
        elif flag == 1: # 도착지 최단 거리 찾기
            if (x,y) == (people[people_index][2],people[people_index][3]):
                shortest.append(distance)
                break
        if stop == 1:
            break
        if visited[x-1][y-1] == 0:
            visited[x-1][y-1] = 1
            for d in range(4):
                nx, ny = x + dir[d][0], y + dir[d][1]
                if -1 < nx-1 < n and -1 < ny-1 < n and board[nx-1][ny-1] == 0:
                    queue.append([nx,ny,distance + 1])

    if flag == 0:
        each_distance = sorted(each_distance, key = lambda x : (x[3],x[1],x[2]))
        if len(each_distance) > 0:
            return each_distance[0]
        else:
            return (-1,-1,-1,-1)
    if flag == 1:
        if len(shortest) > 0:
            return min(shortest)
        else:
            return -1

for _ in range(people_cnt):
# 거기로가고 driver 위치를 갱신한다.

    p, x, y, distance = find_nearest(driver, people, 0, 0)
    if (p,x,y,distance) == (-1,-1,-1,-1):
        gas = -1
        break
    gas -= distance
    driver = [x,y]
    if gas <= 0:
        gas = -1
        break
# 도착지까지 가는 최단 거리를 구한다.
 
    distance = find_nearest(driver, people, p, 1)
    if distance == -1:
        gas = -1
        break

    gas -= distance

    if gas < 0:
        gas = -1
        break
    gas += distance*2

# dirver 위치를 갱신
    driver = [people[p][2],people[p][3]]

    del people[p] 


# 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다.
# 양이 없으면 -1
if len(people) == 0:
    print(gas)
else:
    print(-1)