A = [2,1,5,1,2,2,2]
K = 3
M = 5
def block(A,K,max_sum):
    block_sum = 0
    block_cnt = 0
    for i in A:
        if block_sum + i > max_sum:
            block_sum = i
            block_cnt += 1
        else:
            block_sum += i
        if block_cnt >= K:
            return False
    return True


def binary_search(A,K):
    start = max(A)
    end = sum(A)
    if K == 1:
        return end
    if K >= len(A):
        return start

    while start <= end:
        mid = (start + end) // 2

        if block(A,K,mid):
            end = mid - 1
        else:
            start = mid + 1
    return start


def solution(K,M,A):
    return binary_search(A,K)

print(solution(K,M,A))
    
    
