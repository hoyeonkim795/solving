def solution(n, results):
    answer = 0
    wins = {}
    loses = {}
    for i in range(1,n+1):
        wins[i] = set()
        loses[i] = set()
    for i in range(1,n+1):
        for fight in results:
            if fight[0] == i:
                wins[i].add(fight[1])
            if fight[1] == i:
                loses[i].add(fight[0])
        for winners in loses[i]:
            wins[winners].update(wins[i])
        for losers in wins[i]:
            loses[losers].update(loses[i])
    for num in range(1,n+1):
        if len(loses[num])+len(wins[num]) == n-1:
            answer +=1

        
    return answer

print(solution(	5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 4:3,2
# 3:2
# 1:2
# 2:5