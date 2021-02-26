from collections import deque

def solution(n, costs):
    costs = deque(sorted(costs, key = lambda x : x[2]))
    # 사이클 형성하는 간선은 빼주고 mst 에 넣자
    mst = []
    p = [i for i in range(n+1)]
    tree_edges = 0
    mst_cost = 0
    def find(u):
        if u!= p[u]: # 자기 자신과 같지 않으면
            p[u] = find(p[u])
        return p[u]

    def union(u,v):
        root1 = find(u)
        root2 = find(v)
        p[root2] = root1
    while True:
        if tree_edges == n-1 :
            break
        u, v, wt = costs.popleft()
        if find(u) != find(v):
            union(u, v)
            mst.append((u,v))
            mst_cost += wt
            tree_edges += 1
        

    return mst_cost

print(solution(5,[[0,1,1],[0,4,5],[2,4,1],[2,3,1],[3,4,1]]))

    # answer = float('inf')
    # visited = [[float('inf')]*n for _ in range(n)]
    # dic = dict()
    # for i in range(len(costs)):
    #     visited[costs[i][0]][costs[i][1]] = costs[i][2]
    #     visited[costs[i][1]][costs[i][0]] = costs[i][2]

    #     if costs[i][0] not in dic.keys():
    #         dic[costs[i][0]] = [costs[i][1]]
    #     else:
    #         dic[costs[i][0]].append(costs[i][1])

    #     if costs[i][1] not in dic.keys():
    #         dic[costs[i][1]] = [costs[i][0]]
    #     else:
    #         dic[costs[i][1]].append(costs[i][0])

    # for i in range(n):
    #     total = [0]*n
    #     ans = 0
    #     while True:
    #         total[i] = 1
    #         if total == [1]*n:
    #             break
    #         v = float('inf')

    #         for j in range(len(dic[i])):
    #             if total[dic[i][j]] == 0 and visited[i][dic[i][j]] < v:
    #                 v = visited[i][dic[i][j]]
    #                 idx = dic[i][j]
    #         if v == float('inf'):
    #             ans = float('inf')
    #             break
    #         i = idx
    #         ans += v
    #     print(ans)
    #     if ans < answer:
    #         answer = ans