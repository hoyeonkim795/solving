def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        t = 0

        for j in range(i+1,len(prices)):
            print(prices[i],prices[j])
            t+= 1
            if prices[i] <= prices[j]:
                pass
            else:
                break
        answer.append(t)
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))