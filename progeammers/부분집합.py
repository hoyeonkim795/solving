def backtrack(a, k, input):
    if k == input:
        for i in range(input):
            if a[i]:
                print(S[i], end=' ')
        print()
    else:
        a[k] = 1
        backtrack(a, k+1, input)
        a[k] = 0
        backtrack(a, k+1, input)
a = [0] * 10
S = [1,2,3,4,5,6,7,8,9,10]
backtrack(a, 0, 10)