import sys
sys.stdin = open('input.txt','r')
n = int(input())
arr = input()
check = []
for i in range(1,len(arr)-1,2):
    check.append(i)
    
total = []
def backtrack(a,k,input):
    global total
    if k == input:
        part = []
        for i in range(input):
            if a[i]:
                part.append(check[i])
        total.append(part)
    else:
        a[k] = 1
        backtrack(a, k+2, input)
        a[k] = 0
        backtrack(a, k+2, input)
    return total

a = [0] * 4
print(backtrack(a,0,4))