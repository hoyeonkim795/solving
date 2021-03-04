from itertools import permutations


def solution(n, weak, dist):
    answer = float('inf')
    dists = list(permutations(dist))

    for dist in dists:
        for w in range(len(weak)):
            test_weak = weak[w:]+weak[:w]
            visited = [1]*n
            for i in test_weak:
                visited[i] = 0
            cnt = 0
            flag = 0
            for d in dist:
                for t in test_weak:
                    if visited[t] == 0:
                        x = d + t
                        if x >= n:
                            x %= n
                            visited[t:] = [1]*(n-t)
                            visited[:x+1] = [1]*(x+1)
                        else:
                            visited[t:x+1] = [1] *(x-t+1)
                        cnt += 1
                        if visited == [1]*n:
                            flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1 and cnt < answer:
                answer = cnt

    if answer == float('inf'):
        return -1
    else:
        return answer