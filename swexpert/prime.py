import sys
from pprint import pprint

sys.stdin = open('5249.txt', 'r')


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range (E):
        i, j, W = map(int, input().split())
        adj[i][j], adj[j][i] = W, W

    INF = float('inf')
    key = [INF] * (V+1)
    p = [-1] * (V+1)
    mst = [False] * (V+1)

    key[0] = 0
    cnt = 0
    result = 0
    while cnt < V+1:
        # 아직 mst가 아니고 key가 최소인 정점 선택 :u
        min = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and key[i] < min:
                min = key[i]
                u = i

        # u를 mst로 선택
        mst[u] = True
        result += min
        cnt += 1

        # key값을 갱신
        # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
        for w in range(V+1):
            if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
                key[w] = adj[u][w]
                p[w] = u

    print('#{} {}'.format(tc, result))