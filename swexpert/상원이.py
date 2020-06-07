from collections import deque
import sys
sys.stdin= open('input.txt','r')


t = int(input())
for tc in range(t):
    n,m = map(int,input().split())
    new =  {i: [] for i in range(1, N + 1)}
    for _ in range(m):
        a,b = map(int,input().split())

        if a not in new.keys():
                new[a] =[b]
        else:
            new[a].append(b)
        else:
            if 1 not in new.keys():
                new[1] =[a]


    friends = []
    if 1 in new.keys():
        for i in range(len(new[1])):
            friends.append(new[1][i])
    if 1 in new.values():
        for i in range(le)


    cnt = len(friends)
    for i in range(len(friends)):
        if friends[i] in new.keys():
            for j in range(len(new[friends[i]])):
                friends.append(new[friends[i]][j])

    cnt = len(list(set(friends)-set([1])))

    print(f'#{tc+1} {cnt}')
        
        
