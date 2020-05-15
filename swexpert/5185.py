import sys
sys.stdin = open('input.txt','r')
from collections import deque
t = int(input())
for t in range(t):
    n, notation = input().split()
    n = int(n)
    result = 0
    info = {'A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111', '0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001'}
    for i in range(n):
        result += int(info[notation[i]])
        cal = deque(str(result))
        for j in range(len(str(result))-1,0,-1):
            if result[j] > 1:
                result[j+1] += 1
                result[j] -= 1
                cal.append(result[j]) 
            else:
                cal.appendleft(result[j])
            
        if str(result[0]) > 1:
            while str(result[0]) != 1:
                str(result[0])-= 1
        

    print(f'#{t+1} {"".join(ans)}')
