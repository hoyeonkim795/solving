import sys
sys.stdin = open("input.txt",'r')
n = int(input())
board = [[int(x) for x in input().split()]for _ in range(n)]


total = 0
for i in range(n):
    for j in range(n):
        total += board[i][j]
# 먼저 경계선을 기준으로 5구역을 NEW_BOARD 에 할당한뒤
# 나머지 구역이 new_board[i][j] == 5 일 경우를 피해서 각각 구역을 할당해줬다
# 구역을 구하면서 각각 구역의 총합을 구했고
# 5구역은 총합에서 1,2,3,4 의 구역 합을 빼는 방법으로 진행하였다.

# 정해진 범위의 구역도 나누고 합까지 구하기
def board_sum(x,y,d1,d2):
    new_board = [[0]*n for _ in range(n)]
    b_1 = 0
    b_2 = 0
    b_3 = 0
    b_4 = 0
    b_min = 9999999999999999999999
    b_max = 0
    # 5번 구역
    for i in range(d1+1):
        new_board[x+i-1][y-i-1] = 5
    
    for i in range(d2+1):
        new_board[x+i-1][y+i-1] = 5
    
    for i in range(d2+1):
        new_board[x+d1+i-1][y-d1+i-1] = 5
    
    for i in range(d1+1):
        new_board[x+d2+i-1][y+d2-i-1] = 5

    # 1번 구역
    for i in range(1,x+d1):
        for j in range(1,y+1):
            if new_board[i-1][j-1]==5:
                break
            new_board[i-1][j-1] = 1
            b_1 += board[i-1][j-1]
    if b_1 > b_max:
        b_max = b_1
    if b_1 < b_min:
        b_min = b_1
            
    #2번 구역
    # 열이 거꾸로 시작해야 5의 경계선을 마지막으로 만나기 때문에 j 의 range를 -1 씩
    # 해주도록 range를 설정하였다.
    for i in range(1,x+d2+1):
        for j in range(n,y,-1):
            if new_board[i-1][j-1]==5:
                break
            new_board[i-1][j-1] = 2
            b_2 += board[i-1][j-1]
    if b_2 > b_max:
        b_max = b_2
    if b_2 < b_min:
        b_min = b_2

    #3번 구역
    for i in range(x+d1,n+1):
        for j in range(1,y-d1+d2):
            if new_board[i-1][j-1]==5:
                break
            new_board[i-1][j-1] = 3
            b_3 += board[i-1][j-1]
    if b_3 > b_max:
        b_max = b_3
    if b_3 < b_min:
        b_min = b_3

    # 4번 구역
    # 4번 구역도 2번 구역과 마찬가지로 열이 거꾸로 해야 마지막에 5의 경계선 값을 만나게 되므로
    # range를 -1 씩 거꾸로로 설정해주었다.
    for i in range(x+d2+1,n+1):
        for j in range(n,y-d1+d2-1,-1):
            if new_board[i-1][j-1] == 5:
                break
            new_board[i-1][j-1] = 4
            b_4 += board[i-1][j-1]
    if b_4 > b_max:
        b_max = b_4
    if b_4 < b_min:
        b_min = b_4

    b_5 = total - b_1 - b_2 - b_3 -b_4
    if b_5 > b_max:
        b_max = b_5
    if b_5 < b_min:
        b_min = b_5
    result = b_max - b_min
    return result


min_ans = 99999999999999999999

# d1,d2,x,y 의 범위는 
# 문제에서 주어진
# (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# 를 보며 값을 지정하였다. 
# x의 범위는  x+d1+d2 ≤ N 얘를 보고
# y 의 범위는 1 ≤ y-d1 와 y+d2 ≤ N 를 보고 지정했다.

for d1 in range(1,n):
    for d2 in range(1,n):
        for x in range(1,n-d1-d2+1):
            for y in range(d1+1,n-d2+1):
                ans = board_sum(x,y,d1,d2)
                # 최소값 갱신
                if min_ans > ans:
                    min_ans = ans

print(min_ans)
