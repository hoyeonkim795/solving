import heapq
def taxiDriver(pickup, drop, tip):
    # Write your code here
    heap = []
    for i in range(len(pickup)):
        heapq.heappush(heap, -(drop[i]-pickup[i]+tip[i]))
    return -heap[0]