def solution(n):
    answer = ''
    arr = ['4','1','2']
    while n > 0:
        answer =  arr[n % 3] + answer
        n -= 1
        n //= 3
        
    return answer

print(solution(10))