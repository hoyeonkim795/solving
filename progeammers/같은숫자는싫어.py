def solution(arr):
    answer = [arr[0]]
    i = 0
    while i != len(arr):
        while True:
            if i == len(arr):
                break
            if answer[-1] != arr[i]:
                answer.append(arr[i])
                break
            else:
                i+= 1
    return answer

print(solution([1,1,3,3,0,1,1]))