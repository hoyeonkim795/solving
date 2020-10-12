data = "aabbaccc"
cut = 0

def solution(data):
    now_data = data
    for i in range(1,len(data)//2+1): #자르는 개수
        new_data = ''
        j = 0
        while j < len(data)-i:
            check = i
            cnt = 1
            while True:
                if data[j:j+i+check] == (cnt+1)*data[j:j+i]:
                    cnt+=1
                    check += i
                else:
                    check -= i
                    break
            if cnt == 1:
                new_data += data[j:j+i]
                j += i 
                # print(new_data)
            else:
                new_data += str(cnt)
                new_data += data[j:j+i]
                j = j+i+check
                # print(new_data)
        print(new_data)
        if len(new_data) < len(now_data):
            now_data = new_data
        
    return (len(now_data))
print(solution(data))
    