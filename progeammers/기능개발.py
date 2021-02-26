from collections import deque
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    day = 0
    while progresses:
        if progresses[0] + speeds[0]*day>= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            day += 1
            if cnt > 0:
                answer.append(cnt)
            cnt = 0

    answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))