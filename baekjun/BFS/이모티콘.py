from collections import deque
import sys
sys.stdin = open("input.txt",'r')
# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.
s = int(input())
cb = 0
screen = 1
cnt = 0
q =deque()
q.append([screen,cb,cnt])
visited = set()

while True:
    screen,cb,cnt = q.popleft()
    if s == screen:
        print(cnt)
        break
    if (screen,cb) not in visited:
        
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if screen != 0:
            ncb = screen
            q.append([screen,ncb,cnt+1])


        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if cb!= 0:
            nscreen = screen+cb
            q.append([nscreen,cb,cnt+1])

        # 화면에 있는 이모티콘 중 하나를 삭제한다.
        if screen > 1:
            n_screen =screen- 1
            q.append([n_screen,cb,cnt+1])
        
        visited.add((screen,cb))

    

