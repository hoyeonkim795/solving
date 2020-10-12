def Counting_Sort(A, B, k):
# A [1 .. n] 입력 배열
# B = [0]*len(a) 정렬된 배열
# C count list 카운트 배열

    C = [0] * k

    # 카운트 리스트에 각 숫자 발생 빈도를 C 리스트에 저장
    for i in range(0, len(B)): 
        C[A[i]] += 1

    # C 리스트에서 앞 인덱스 크기를 더해주기, 누적하여 인덱스 만들기 
    for i in range(1, len(C)):
        C[i] += C[i-1]
    print(C)

    for i in A:
        print(C[i]-1,end=' ')
        B[C[i]-1] = i
        C[i] -= 1
        
    return B


a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)
k = max(a) + 1

print(Counting_Sort(a, b, 5))