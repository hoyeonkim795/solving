
import itertools
import copy
def find_longest(bad):
    longest_max = 0

    for i in range(len(bad)):
        c_max = 0
        for j in range(i,len(bad)):
            if bad[i]=='1' and bad[i] == bad[j]:
                c_max +=1
            else:
                break

        if c_max> longest_max:
            longest_max = c_max
    return longest_max
def pick(n,arr):
    result = []

    for i in itertools.permutations(arr,n):
        result.append(list(i))
    return result

def solution(road, n):
    answer = -1
    result = []
    arr = []
    for i in range(len(road)):
        if road[i] == '0':
  
            arr.append(i) #0인아이 찾기

    result = pick(n,arr)
    final_max = 0

    for r in range(len(result)):
        #road 초기화
        new_road = list(copy.deepcopy(road))

        for n in range(n):
            new_road[result[r][n]] = '1' # 0인 애 1로 고치기
        now_max = find_longest(new_road) # 1 가장 긴 값들

        if final_max<now_max:
            final_max = now_max
    

    return final_max

road = "111011110011111011111100011111"
n = 3
print(solution(road, n))