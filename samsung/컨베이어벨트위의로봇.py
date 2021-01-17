import sys
from collections import deque
sys.stdin = open("input.txt",'r')
n,k = map(int,input().split())
arr = deque(list(map(int,input().split())))

ans = 1

robot = deque(list([0]*n))

while True:     # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    # 1단계 벨트가 한 칸 회전한다.
    arr.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    # print('1단계')
    # print(robot)
    # print(arr)
    # 2단계 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(-2, -n-1, -1):

        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1-n] > 0:
            robot[i] = 0
            robot[i+1] = 1
            arr[i+1-n] -= 1
    robot[-1] = 0
    # print('2단계')
    # print(robot)
    # print(arr)
    # 3단계 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and arr[0] > 0:
        robot[0] = 1 
        arr[0] -= 1
    # print('3단계')
    # print(robot)
    # print(arr)
    # 4단계
    if arr.count(0) >= k:
        break
    ans += 1
    

print(ans)
