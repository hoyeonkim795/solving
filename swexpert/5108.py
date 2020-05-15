
for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    num_list = list(map(int, input().split()))
    for _ in range(M):
        idx, num = map(int, input().split())
        num_list.insert(idx, num)
    print('#{} {}'.format(tc, num_list[L]))