import heapq
def solution(jobs):
    answer = 0
    heap = []
    jobs = sorted(jobs, key=lambda x : x[0])
    heap = []
    now = 0
    # 걸리는 시간 + 전의 작업이 끝나는시간 - 요청 시작시간
    cnt = 0
    while True:
        if cnt == len(jobs):
            break
        for i in range(len(jobs)):
            start, time = jobs[i]
            if start <= now :
                heapq.heappush(heap,now+time-start)
  
        print(heapq.heappop(heap))
        cnt += 1


    # return answer

print(solution([[0, 3], [1, 9], [2, 6]]))