def solution(next_student):
    N = len(next_student)
    adj = [-1 for _ in range(N)] # 인접 리스트 만들기
    for n in range(N):
        if next_student[n] != 0: # 카드를 넘겨줄 학생일 경우
            adj[n] = next_student[n] - 1
    print(adj)
    card_cnt = [1] * N # 학생마다 카드를 넘기는 수를 저장할 리스트
    for n in range(N): # BFS로 하나하나 카드가 몇번 넘어가는지 cnt 카운트하기
        if adj[n] != -1:
            visited = [False] * N
            cnt = 1
            q = [n]
            while q: # BFS
                print(q)
                x = q.pop(0)
                if visited[x] == False and adj[x] != -1:
                    visited[x] = True
                    if visited[adj[x]] == False:
                        q.append(adj[x])
                        cnt += 1
            card_cnt[n] = cnt 

    for c in range(N - 1, -1, -1): # 가장 많이 카드를 넘긴 하
        if card_cnt[c] == max(card_cnt):
            answer = c + 1
            break
    return answer


next_student = [6, 10, 8, 5, 8, 10, 5, 1, 6, 7]
next_student = [5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]
print(solution(next_student))