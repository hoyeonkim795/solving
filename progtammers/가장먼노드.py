from collections import deque
def solution(n, edge):
    answer = 0
    graph = dict()
    for nums in edge:
        if nums[0] not in graph:
            graph[nums[0]] = [nums[1]]
        else:
            graph[nums[0]].append(nums[1])
        if nums[1] not in graph:
            graph[nums[1]] = [nums[0]]
        else:
            graph[nums[1]].append(nums[0])


    return answer

print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))