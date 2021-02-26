
from collections import deque
def order(city_nodes, city_from, city_to, company):
    # Write your code here
    dic = dict()
    for i in range(len(city_from)):
        if city_from[i] not in dic.keys():
            dic[city_from[i]] = [city_to[i]]
        else:
            dic[city_from[i]].append(city_to[i])
        if city_to[i] not in dic.keys():
            dic[city_to[i]] = [city_from[i]]
        else:
            dic[city_to[i]].append(city_from[i])
    
    check = [0]*(city_nodes+1)
    queue = deque()
    for i in range(len(dic[company])):
        queue.append([dic[company][i],1])
    ans = []
    result = []
    now = 1
    check[company] = 1
    distance = [[] for _ in range(10**5+2)]
    final = 0
    while queue:
        node, cnt = queue.popleft()
        if check[node] == 0:
            check[node] = 1
            distance[cnt].append(node)
            if final < cnt:
                final = cnt
            if node in dic.keys():
                for i in range(len(dic[node])):
                    if check[dic[node][i]] == 0:
                        queue.append([dic[node][i], cnt+1])
            
    for i in range(1,final+1):
        ans += sorted(distance[i])

    return ans

print(order(10,[1,1,3,3,7,2,2,2,4],[2,3,6,7,8,10,5,4,9],1))
