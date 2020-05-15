def modify_seq():
    for _ in range(M):
        command, *args = input().split()

        if command == 'I':
            seq.insert(int(args[0]), int(args[1]))
        elif command == 'D':
            seq.pop(int(args[0]))
        elif command == 'C':
            seq[int(args[0])] = int(args[1])

    try:
        return seq[L]
    except IndexError:
        return -1


T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    seq = list(map(int, input().split()))

    print(f'#{test_case} {modify_seq()}')