# def binarySearch (arr, key):
#     start = 0
#     end = len(arr)-1
#     while start <= end:
#         middle = (start + end)//2
#         if arr[middle] == key:
#             return key
#         elif arr[middle] < key:
#             start = middle + 1
#         else:
#             start = middle - 1

# a = [2, 4, 6, 8, 9, 11]
# print(binarySearch(a, 11))

def binarySearch (arr, start, end, key):
    if start > end:
        return False
    else:
        middle = (start + end) //2
        if key == arr[middle]:
            return "정답"
        elif key < arr[middle]:
            return binarySearch(arr, start, middle-1 ,key)
        elif arr[middle] < key:
            return binarySearch(arr, middle+1, end, key)

def binarySearch2(a, start, end, key):
    if start > end:
        return False
    else:
        middle = (start + end)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, start, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, end, key)

a = [2, 4, 6, 8, 9, 11]
print(binarySearch(a, 0, len(a)-1, 11))