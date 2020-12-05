import sys
from collections import deque
sys.stdin = open("input.txt",'r')
n,k = map(int,input().split())
<<<<<<< HEAD
a = [int(x) for x in input().split()]
queue = deque(a)
r_queue = deque([False]*2*n)
cnt = 1
# 0: 올라가는 위치
# n-1: 내려가는 위치
while True:
    # 벨트가 한 칸 회전한다.
    queue.rotate(1)
    r_queue.pop()
    r_queue.appendleft(False)
    r_queue.rotate(1)

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    if r_queue[-1] == True:
        r_queue[-1] = False
    for i in range(n-2,-1,-1):
        if r_queue[i] == True and r_queue[i+1] == False and queue[i+1] > 0:
            r_queue[i+1] = True
            queue[i+1] -= 1

    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if r_queue[0] == False and queue[0] > 0:
        r_queue[0] = True
        queue[0] -= 1
    cnt +=1
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if queue.count(0) >= k:
        break
print(cnt)
=======
a = deque([int(x) for x in input().split()])
r = deque([False]*n*2)

cnt = 1
while True:
    # 벨트가 한 칸 회전한다.
    a.rotate(1)
    r.rotate(1)
    r[n-1] = False

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(n-2,-1,-1):
        if r[i] == True and r[i+1] == False and a[i+1] > 0 :
            a[i+1] -= 1
            r[i+1] = True
            r[i] = False
    r[n-1] = False   #얘가 중요
    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if r[0] == False and a[0] > 0:
        r[0] = True
        a[0]-= 1

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if a.count(0) >= k:
        print(cnt)
        break
    cnt += 1
>>>>>>> ceb9457380adba16c1ee27194d6b9b1e1d3d287b
