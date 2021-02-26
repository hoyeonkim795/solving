def solution(N, number):
    S = [0, {N}]
    if N == number:
        return 1
    for i in range(2, 9):
        case = {int(str(N)*i)}
        for j in range(1, i//2+1):
            for x in S[j]:
                for y in S[i-j]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(y-x)
                    case.add(x*y)
                    if x != 0:
                        case.add(y//x)
                    if y != 0:
                        case.add(x//y)
        if number in case:
            return i
        S.append(case)
    return -1


print(solution(5,5))
    # 1 : (0+1)
    # 2 : (0+2, 1+1)
    # 3 : (0+3, 1+2)
    # 4:  (0+4, 1+3, 2+2)
    # 5:  (0+5, 1+4, 2+3)
    # 6 : (0+6, 1+5, 2+4, 3+3)
    # 7 : (0+7, 1+6, 2+5, 3+4)
    # 8 : (0+8, 1+7, 2+6, 3+5, 4+4)
# a = {'5'}
# b = {'55','555'}
# print(a|b)