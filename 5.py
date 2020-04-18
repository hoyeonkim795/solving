dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc4", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc2", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

tags = ["t1", "t2", "t3"]
def solution(dataSource, tags):
    data_dict = {}
    cnt_arr = [0]*len(dataSource) 

    for i in range(len(dataSource)):
        v = []
        for j in range(1,len(dataSource[i])):
            v.append(dataSource[i][j])
        
        data_dict[dataSource[i][0]] = v
    idx = -1
    for i in data_dict.keys():
        t = data_dict[i]
        idx += 1
        cnt = 0
        for j in range(len(tags)):
            if tags[j] in t:
                cnt += 1
        cnt_arr[idx] = cnt
    
    new_dict = {}
    for i in range(len(cnt_arr)):
        new_dict[dataSource[i][0]] = cnt_arr[i]
    new_dict = sorted(new_dict.items(),key=lambda x: x[1],reverse=True)
    
    ans = []

    for i in range(len(new_dict)):
        if new_dict[i][1] != 0:
            ans.append(new_dict[i][0])

    


    return ans
print(solution(dataSource,tags))

