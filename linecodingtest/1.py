def solution(inputString):
    a,b,c,d = 0,0,0,0
    result = []
    for i in range(len(inputString)):
        if inputString[i] == '(' and (a == 0 or a ==2):
            a = 1
        elif inputString[i] == '{' and (b== 0 or b == 2):
            b = 1
        elif inputString[i] =='[' and (c == 0 or c == 2) :
            c = 1
        elif inputString[i] == '<' and  (d ==0  or d == 2):
            d = 1
        elif inputString[i] == ')' and a == 1:
            a = 2
        elif inputString[i] =='}' and b== 1:
            b=2
        elif inputString[i] == ']' and c == 1:
            c=2
        elif inputString[i] == '>' and d ==1 :
            d=2

        elif inputString[i] == ')' and (a == 0 or a == 2):
            a = -1
            break
        elif inputString[i] =='}' and (b== 0 or b == 2):
            b=-1
            break
        elif inputString[i] == ']' and (c == 0 or c == 2):
            c=-1
            break
        elif inputString[i] == '>' and (d ==0  or d == 2):
            d=-1
            break
        
    result = [a,b,c,d]
    cnt = 0

    for i in range (len(result)):
        if result[i] == 0:
            cnt += 0
        elif result[i] == 2:
            cnt += 1
        elif result[i] == -1:
            cnt = -1
    return cnt

inputString = "<>_><"
print(solution(inputString))