tc = int(input())

for tc in range(tc):
    price = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    #plan 1 계산하기
    money = 0
    c_month = 0

    for i in range(len(plan) - 2):
        if plan[i] != 0 and plan[i + 1] != 0 and plan[i + 2] != 0:
            c_month += 1
            a, b, c = plan[i], plan[i + 1], plan[i + 2]
        if
    for i in range(len(plan)):
        if plan[i] != 0:
            day = plan[i]
        if day*price[0] > price[1]:
            money += price[1]
        else:
            money += day*price[0]

    #plan 2 계산하기
    month = 0
    for i in range(len(plan)):
        if plan[i] !=0:
            month += 1
    result2 = month*price[1]
    #plan3 계산하기
    c_month = 0


