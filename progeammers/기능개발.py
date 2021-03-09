from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    done = []
    for idx, progress in enumerate(progresses):
        days = math.ceil((100 - progress)/speeds[idx])
        done.append(days)
    now = done[0]
    cnt = 0
    for i in range(len(done)):
        if done[i] <= now:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            now = done[i]
    answer.append(cnt)
    
    return answer

print(solution([95, 90, 99, 99, 80, 99]	,	[1, 1, 1, 1, 1, 1]	))