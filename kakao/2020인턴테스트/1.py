

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]
    info_2= [[2],[1,3,5],[4,6,8],[7,9,0],['*','#']]
    info_5 = [[5],[4,6,8,2],[1,3,7,9,0],['*','#']]
    info_8 = [[8],[5,7,9,0],['*','#',4,6,2],[1,3]]
    info_0 = [[0],['*','#',8],[7,9,5],[4,6,2],[1,3]]
    answer = ''
    lf = '*'
    rf = '#'
    for i in range(len(numbers)):
        if numbers[i] in left:
            answer +='L'
            lf = numbers[i]

        elif numbers[i] in right:
            answer += 'R'
            rf = numbers[i]

        else:
            if numbers[i] == 2:
                info = info_2
            elif numbers[i] == 5:
                info = info_5
            elif numbers[i] == 8:
                info = info_8
            elif numbers[i] == 0:
                info = info_0

            for k in range(len(info)):
                if lf in info[k] and rf in info[k]: # 같은 거리
                    if hand == 'right':
                        rf = numbers[i]
                        answer += 'R'
                        break
                    elif hand == 'left':
                        lf = numbers[i]
                        answer += 'L'
                        break
                if lf in info[k] :
                    lf = numbers[i]
                    answer += 'L'
                    break
                elif rf in info[k]:
                    rf = numbers[i]
                    answer += 'R'
                    break


    
    return answer


print(solution(numbers,hand))