from collections import deque
def solution(priorities, location):
    answer = 0
    arr = [i for i in range(len(priorities))]
    queue = deque(arr)
    priorities = deque(priorities)
    while queue:
        a = queue.popleft()
        b = priorities.popleft()

        for i in range(len(priorities)):
            if b < priorities[i]:
                priorities.append(b)
                queue.append(a)
                break
        else:
            answer += 1
            if location == a:
                return answer

print(solution([1, 1, 9, 1, 1, 1],0))