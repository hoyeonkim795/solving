import sys
sys.stdin = open("input.txt", 'r')


def BinarySearch(l,r,A,x): # x 는 찾는값
    before = None
    while l<=r:
        m = (l+r)//2
        if A[m] == x:
            return True
        elif x > A[m]:
            l = m+1
            now = 1
        elif x< A[m]:
            r=m-1
            now = -1
        if now == before:
            return False
        before = now
            
    return False


t = int(input())
for tc in range(t):
    n,m= map(int,input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    result = 0
    for i in range(len(B)):
        x = B[i]
        l = 0
        r = len(A)-1
        if BinarySearch(l,r,A,x):
            result += 1
        
    print(f'#{tc+1} {result}')
        
    


