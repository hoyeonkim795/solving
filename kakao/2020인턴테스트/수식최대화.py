import re
def solution(expression):
    answer = 0
    p = re.compile('[0-999]+')
    numbers = list(map(int,p.findall(expression)))
    o = re.compile('[*+-]+')
    operand = o.findall(expression)
    print(numbers)
    print(operand)
    op_dic = dict()
    op_dic['+'] = []
    op_dic['-'] = []
    op_dic['*'] = []
    for i in range(len(operand)):
        op_dic[operand[i]].append(i)
        op_dic[operand[i]].sort()
100-200*300-500+20
100-200*300-520
-100*-220
    # '+' > '-' > '*'
    result = 0
    for op in ['+','-','*']:
        if op in op_dic.keys():
            for i in op_dic[op]:
                if op == '+':
                    result += numbers[i]+numbers[i+1]
                    numbers[i] = numbers[i]+numbers[i+1]
                    numbers[i+1] = numbers[i]+numbers[i+1]
                elif op == '-':
                    result += numbers[i]-numbers[i+1]
                    numbers[i] = numbers[i]-numbers[i+1]
                    numbers[i+1] = numbers[i]-numbers[i+1] 
                elif op == '*':
                    result += numbers[i]*numbers[i+1]
                    numbers[i] = numbers[i]*numbers[i+1]
                    numbers[i+1] = numbers[i]*numbers[i+1]
    print(numbers[0])

    # '+' > '*' > '-'
    # '-' > '+' > '*'
    # '-' > '*' > '+'
    # '*' > '-' > '+'
    # '*' > '+' > '-'
    return answer


print(solution("100-200*300-500+20"))