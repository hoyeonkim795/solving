def test(metal_info):
    result = [metal_info[0]]
    while True:
        if len(result) == len(metal_info):
            break
        for j in range(1, len(metal_info)):
            if result[-1][-1] == metal_info[j][0]:
                result.append(metal_info[j])

            elif result[0][0] == metal_info[k][1]:
                result.insert(0, metal_info[k])
    '''final_result = ''
    for c in range(len(result)):
        final_result += ' '.join(map(str, result[c]))'''
    return result


tc = int(input())
for t in range(tc):
    metal_num = int(input())
    mid_metal_info = list(map(int, input().split()))  # 2개씩 2차원 배열로 입력받기
    metal_info = []
    for i in range(1, len(mid_metal_info), 2):
        metal_info += [[mid_metal_info[i - 1], mid_metal_info[i]]]
    result = test(metal_info)
    print(f'#{t+1}',end=' ')
    for k in range(len(result)):
        for j in range(0, 2):
            print(result[k][j], end=' ')
    print()

