key = [[0,0,0],[0,0,0],[0,0,1]]
lock = [[1,1,1,1],[1,0,1,1],[1,1,1,1],[1,1,1,1]]

def rotate(mylist):
    new_list= [[0]*len(mylist) for _ in range(len(mylist))]
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            new_list[i][j] = mylist[len(mylist)-1-j][i]
    return new_list

def solution(key, lock):

    n = len(key)
    m = len(lock)
    for i in range(m):
        lock[i] = [0]*(n-1) + lock[i] + [0]*(n-1)

    top =  [[0]*(2*n+m-2) for _ in range(n-1)]
    lock = top + lock + top

    for i in range(5):
        key = rotate(key)
        for dx in range(2*n-1):
            for dy in range(2*n-1):
                background = [[0]*(2*n+m-2) for _ in range(2*n+m-2)]
                for x in range(n):
                    for y in range(n):
                        background[x+dx][y+dy] += key[x][y]
                cnt = 0

                for a in range(n-1, n+m-1):
                    for b in range(n-1, n+m-1):
                        if lock[a][b] + background[a][b] == 1:
                            cnt += 1
                        else:
                            continue
                if cnt == m*m:
                    return True

    return False


print(solution(key,lock))
[[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0]]