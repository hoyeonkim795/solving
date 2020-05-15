from itertools import permutations
from copy import deepcopy
def calculate(op,x,y):
    if op == '+':
        x = int(x)
        y = int(y)
        return x+y
    elif op == '-':
        x = int(x)
        y = int(y)
        return x-y
    elif op == '*':
        x = int(x)
        y = int(y)
        return x*y


def totallist(op,numbers):
    total = []
    for i in range(len(op)):
        total.append(numbers[i])
        total.append(op[i])
    total.append(numbers[-1])
    return total


def solution(expression):
    s = ['+','-','*']
    answer = 0
    #연산자 우선순위 조합
    total = list(permutations(s,3))
    print(total)
    op = []

    for i in range(len(expression)):
        if expression[i] in s :
            op.append(expression[i])

    # 숫자만 뽑기        
    numbers = expression.replace('*','/').replace('+','/').replace('-','/').split('/')

    for i in range(len(total)):
     # ('+', '-', '*')
        new_numbers = deepcopy(numbers)
        for j in range(3):
            for k in range(len(op)):

                if op[k] == total[i][j]:
                    ns = '(' + new_numbers[k] 
                    new_numbers[k] =ns
                    cnt = 0
                    for t in range(k+1,len(numbers)):
                        if new_numbers[t][0] == '(':
                            cnt +=1
                    new_numbers[k+1+cnt] += ')'
        to_list = totallist(op,new_numbers)
        l_str = ''.join(to_list)
        print(l_str)

        # mid_ans = eval(str(to_list))
        
 

    return numbers



expression = "100-200*300-500+20"
print(solution(expression))