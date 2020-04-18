def sort():
    first_seq = list(map(int, input().split()))

    for _ in range(M - 1):
        seq_len = len(first_seq)
        next_seq = list(map(int, input().split()))

        for i in range(seq_len):
            if first_seq[i] > next_seq[0]:
                first_seq[i:0] = next_seq
                break

        if seq_len == len(first_seq):
            first_seq.extend(next_seq)

    return first_seq


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    ans = sort()

    print('#{} '.format(test_case), end='')
    print(' '.join(str(n) for n in ans[-1:-11:-1]))