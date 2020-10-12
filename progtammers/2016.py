def solution(a, b):
    # 31,29,31,30,31,30,31,31,30,31,30,31
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    # 금,토,일,월,화,수,목
    # SUN,MON,TUE,WED,THU,FRI,SAT
    y = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = ''
    # 각 월의 끝 요일 구하기
    if a == 1:
        pass
    else:
        for i in range(a-1):
            y = y[months[i]%7:] + y[:months[i]%7]

    result = y[b%7]

    return result

print(solution(5,24))