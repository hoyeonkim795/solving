import sys
sys.stdin = open("5189input.txt","r")

def perm(start):
    global sub_result, result, final_result

    if len(sub_result) == N-1:
        for i, j in sub_result:
            result += Battery_Usage[i][j]

        result += Battery_Usage[start][0]
        final_result.append(result)
        result=0
        return

    for next in range(1, N):
        if not visited[next]:
            sub_result.append((start, next))
            visited[next] = True
            perm(next)
            sub_result.remove((start, next))
            visited[next] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Battery_Usage = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    visited = [0] * N
    sub_result = []
    result = 0
    final_result = []
    perm(0)
    print('#{} {}'.format(tc, min(final_result)))