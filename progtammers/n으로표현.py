def calculate(s,num1,num2):
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1-num2
    elif s == '*':
        return num1*num2
    elif s=='/':
        return num1//num2

def solution(N, number):
    S = set()
    for i in range(1,9):
        S.add(int(str(N)*i))
    for i in range(1, len(S)):
        for j in range(i):
            for num1 in S[j]:
                for num2 in S[i-j-1]

    return -1


print(solution(2, 11))