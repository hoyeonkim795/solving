T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for m in range(M):
        index, data = map(int, input().split())
        tree[index] = data
    i = N-M
    if i > 0:
        tree[i] = tree[i*2]
        if i*2+1 <= N:
            tree[i] += tree[i*2+1]
    for i in range(N-M-1, L-1, -1):
        tree[i] = tree[i*2] + tree[i*2+1]
    print("#{0} {1}".format(t, tree[L]))
