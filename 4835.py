def sectiom_sum(count,section_count,num_info):
    info_list = []

    for j in range(count - section_count+1):
        info_sum = 0
        
        for k in range(section_count):
            info_sum += num_info[j+k]
            
            
        info_list.append(info_sum)
            
   
    result = max(info_list) - min(info_list)
    return result


tc = int(input())

for i in range(0,tc):
    a = list( map(int,input().split()))
    count, section_count = a[0],a[1]
    num_info = list(map(int,input().split()))
    print(f'#{i+1} {sectiom_sum(count,section_count,num_info)}')
