import sys
sys.stdin = open('input.txt','r')
T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tree_info = list(map(int, input().split()))
    isSubtree = []
    for e in range(E+2):
        isSubtree.append(False)
    print(isSubtree)
    isSubtree[N] = True
    print(isSubtree)
    ans = 1
    for i in range(len(tree_info)//2):
        if isSubtree[tree_info[2*i]]:
            if isSubtree[tree_info[2*i+1]] is False:
                isSubtree[tree_info[2*i+1]] = True
                ans += 1
    print("#{0} {1}".format(t, ans))

