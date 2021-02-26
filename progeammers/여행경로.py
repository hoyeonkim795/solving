tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
def solution(tickets):
    answer = []
    graph = dict()
    for airports in tickets:
        if airports[0] not in graph:
            graph[airports[0]] = [airports[1]]
        else:
            graph[airports[0]].append(airports[1])

    for k in graph.keys():
        graph[k].sort(reverse=True)

    stack = ["ICN"]
    visited = []
    ans = []
    while stack:
        root = stack[-1]
        if root not in graph or len(graph[root]) == 0:
            ans.append(stack.pop())
        else:
            stack.append(graph[root][-1])
            graph[root].pop()
            
    ans.reverse()
    return ans

print(solution(tickets))

# # s = ['ICN']
# # s += ['ATL', 'SFO', 'SFO']
# # print(s)