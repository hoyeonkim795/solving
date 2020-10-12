
def solution(n, lost, reserve):

    lost_set = list(set(lost)-set(reserve))
    reserve_set = list(set(reserve)-set(lost))

    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)

    return n-len(lost_set)

print(solution(5,[2, 3, 4],[1, 3, 5]))