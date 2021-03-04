def backtrack(a, k, s):
    if k == s:
        psum = 0
        for i in range(s):
            if a[i]: 
                psum += S[i]
        if psum == 10:
            for i in range(s):
                if a[i]: 
                    print(S[i], end=' ')
            
    else:
        a[k] = 1
        backtrack(a, k+1, s)
        a[k] = 0
        backtrack(a, k+1, s)
    
a = [0] * 10000
S = [i for i in range(1,10001)]
backtrack(a, 0, s)

def solution(n, s):
    answer = []
    return answer