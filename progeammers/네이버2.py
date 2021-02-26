n = 15
edges = [[0,2],[2,1],[2,4],[4,3],[4,5],[5,6],[5,8],[10,9],[11,7],[7,12],[7,13],[13,14]]
node = [0]*(n)
print(node)
dic = dict()
for i in range(len(edges)):
    if edges[i][0] not in dic:
        dic[edges[i][0]] = [edges[i][1]]
        node[edges[i][0]] += 1
    else:
        dic[edges[i][0]].append(edges[i][1])  
        node[edges[i][0]] += 1

    if edges[i][1] not in dic:
        dic[edges[i][1]] = [edges[i][0]]
        node[edges[i][1]] += 1
    else:
        dic[edges[i][1]].append(edges[i][0])  
        node[edges[i][1]] += 1
print(dic)
print(node)
