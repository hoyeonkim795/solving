def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def solution(A):
    A.sort()

    a = A[-1]*A[-2]*A[-3]
    b= A[0]*A[1]*A[-1]
    if a>b:
        return a
    else:
        return b
