N, M = map(int, input().split())
print(N,M)
info = [[2, 0, 0, 0, 1, 1, 0],[0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
#info = [[int(x) for x in input().split()]for i in range(N)]
print(info)

dir = [[1,0],[0,1],[-1,0],[0,-1]]
stack = []
visited = [[0]*M for i in range(N)]
everyresult = []

#무작위 벽세우기		
def backtrack(a,k,input):
	makingwall = []
	result_wall = []
	if k == input :
		psum = 0
		for i in range(input):
			if a[i]:
				psum += 1
		if psum == 3:
			for i in range(len(a)):
				if a[i] == 1:
					makingwall.append(who_zero[i])
			result_wall.append(makingwall)
	else:
		a[k] = 1
		backtrack(a,k+1,input)
		a[k] = 0
		backtrack(a,k+1,input)
	return result_wall
	
# 감염 되지않은 바이러스 개수 찾기
def find_nonvirus(info,N,M):
	cnt = 1
	for i in range(N):
		for j in range(M):
			if info[i][j] == 0:
				cnt += 1
	return cnt
		
who_zero = []
for i in range(N):
	for j in range(M):
		if info[i][j] == 0:
			who_zero.append([i,j])

a = [0]*len(who_zero)
result_wall = backtrack(a,0,len(who_zero))
#print(result_wall)

'''			
# 바이러스 찾기
for i in range(N):
	for j in range(M):
		if info[i][j] == 2:
			stack.append([i,j])
			
for i in range(len(result_wall)):
	for j in range(3):
		x,y = result_wall[i][j]
		info[x][y] = 1  #새로만든 부분집합 3개짜리 벽을 info에 추가함
		while (len(stack)>0):
			x,y = stack.pop()  #값이 2인 아이들, 바이러이스 걸린애
			
			
			if visited[x][y] != 1:
				visited[x][y] = 1
				
				for d in range(len(dir)): #바이러스 걸린애 4방향으로 검사
					dx = dir[d][0]
					dy = dir[d][1]
					nx, ny = x+dx, x+dy
					
					if -1 < nx < N and -1 < ny < M:
						if info[x][y] == 0 and visited[nx][ny] == 0: #감염 시키기
							info[x][y] = 2
		everyresult.appnd(find_nonvirus(info,N,M))
		
print(max(everyresult))
'''