from itertools import combinations
def solution(orders, course):
    answer = []
    for num in course:
        menus = dict()
        max_menu_cnt = 0
        for order in orders:
            menu_group= list(map(list,combinations(list(order).sort(),num)))
            for i in range(len(menu_group)):
                if "".join(menu_group[i]) not in menus.keys():
                    menus["".join(menu_group[i])] = 1
                else:
                    menus["".join(menu_group[i])] += 1
                if menus["".join(menu_group[i])] > max_menu_cnt:
                    max_menu_cnt = menus["".join(menu_group[i])]
        if max_menu_cnt == 1:
            continue
        for key in menus.keys():
            if menus[key] == max_menu_cnt:
                answer.append(key)
        
    answer.sort()

    return answer

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))

