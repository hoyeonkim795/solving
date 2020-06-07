from collections import deque
def solution(tickets):
    answer = []

    airports =[]
    # 공항장소
    for i in range(len(tickets)):
        airports.append(tickets[i][0])
        airports.append(tickets[i][1])
    airports= list(set(airports))   
    
    visited = [0]*len(tickets) 
    
    q = deque()
    q.append('ICN')
    answer.append('INC')
    cnt = 0
    while q:
        x = q.popleft()
        visited[tickets.index(x)] = 1
     
        for i in range(len(tickets)):
            if tickets[i][0] == x and visited[airports.index(tickets[i][1])]==0 :
                q.append(tickets[i][1])
                answer.append(tickets[i][1])

    return answer

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))