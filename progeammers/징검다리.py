stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
def binarySearch (arr, key):
    start = 0
    end = len(arr)-1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == key:
            return key
        elif arr[middle] < key:
            start = middle + 1
        else:
            start = middle - 1
            
def solution(stones,k):
