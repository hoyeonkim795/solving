longest_max = 0
bad = [1,1,0,1,1,1]
for i in range(len(bad)):
    c_max = 0
    for j in range(i,len(bad)):
        if bad[i] == bad[j]:
            c_max +=1
        else:
            break
    if c_max> longest_max:
        longest_max = c_max
print(longest_max)
