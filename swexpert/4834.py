def count(N,data):
    new_dict ={}
    for k in data:
        if k not in new_dict:
            new_dict[k]= 1
        else:
            new_dict[k] += 1

    result_list=[]
    max_value = max(new_dict.values())
    for (k,v) in new_dict.items():
        if v==max_value:
            result_list.append(k)

    max_key = max(result_list)
    result =f'{max_key} {max_value}'
    return result

    


T= int(input())
for i in range(T):
    N = int(input())
    a_i = input()
    data =[]
    for j in range(len(a_i)):
        data.append(int(a_i[j]))
    print(f'#{i+1} {count(N,data)}')
    