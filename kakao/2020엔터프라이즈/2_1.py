import sys
sys.stdin = open('input.txt','r')
N = int(input())
lst = [list(input().split()) for __ in range(N *(N -1))]
result_list = []
result_list2 = []

for i in range(len(lst)):
    if [lst[i][0], 0, 0] not in result_list:
        result_list.append([lst[i][0], 0, 0])


for i in range(len(lst)):
    if int(lst[i][1]) - int(lst[i][3]) > 0:
        result_list2.append([lst[i][0], 1, int(lst[i][1]) - int(lst[i][3])])
        result_list2.append([lst[i][2], 0, int(lst[i][3]) - int(lst[i][1])])
    else:
        result_list2.append([lst[i][2], 1, int(lst[i][3]) - int(lst[i][1])])
        result_list2.append([lst[i][0], 0, int(lst[i][1]) - int(lst[i][3])])


for i in range(len(result_list2)):
    for j in range(len(result_list)):
        if result_list2[i][0] in result_list[j][0]:
            result_list[j][1] = result_list[j][1] + result_list2[i][1]
            result_list[j][2] = result_list[j][2] + result_list2[i][2]


print(result_list)


result_list.sort(key=lambda x:(-x[1], -x[2], x[0]))
for i in range(len(result_list)):
    print(' '.join(map(str, result_list[i])))