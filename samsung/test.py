arr = [[1,2,3],[4,5,6],[7,8,9]]

arr_2 = (list(zip(*arr[::-1])))
print(arr_2)

def rotated(a):
    n = len(a)
    m = len(a[0])
    new = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = a[i][j]
    return new

print(rotated(arr))