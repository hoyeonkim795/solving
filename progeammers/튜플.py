import re
def solution(s):
    s = re.split('{|}',s)
    ans_s = []
    for i in range(len(s)):
        if len(s[i]) > 0 and s[i] != ',':
            mid_s = list(map(int,s[i].split(',')))
            ans_s.append(mid_s)


    new_s = quickSort(ans_s)
    ans = []
    for i in range(len(new_s)):
        for j in range(len(new_s[i])):
            if new_s[i][j] not in ans:
                ans.append(new_s[i][j])
            else:
                pass
    
    return ans