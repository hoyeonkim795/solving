
from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [0] *len(words)
    q = deque()
    q.append((begin,0))

    while q:
        x,cnt = q.popleft()
        if x == target:
            answer = cnt
            break
        for i in range(len(words)):
            if visited[i] == 0 :
                t = 0
                for j in range(len(words[i])):
                    if words[i][j] == x[j]:
                        t+=1
                if t == len(target)-1:
                    q.append((words[i],cnt+1))
                    visited[i] = 1

            
    return answer

print(solution('cote','coge',['coge', 'dote', 'doge', 'lote', 'loge']))