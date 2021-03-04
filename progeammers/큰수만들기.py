def solution(number, k):
    answer = ''
    x = len(number)-k #x개 선택
    start = 0
    end = len(number) -x + 1

    while len(answer) != x:
        ans = -1
        if end - start == 1:
            answer += number[start:]
            break

        for i in range(start,end):
            if int(number[i]) == 9:
                idx = i
                break
            if int(number[i]) > ans:
                ans = int(number[i])
                idx = i
        answer += number[idx]
        start = idx+1
        end += 1 
        
    return answer

print(solution("000010000",2))