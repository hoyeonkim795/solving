# from collections import deque
# from copy import deepcopy
# def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
#     # Write your code here
#     dirs = [[1,0],[0,1],[0,-1],[-1,0]]
#     cost = 0
#     queue = deque()
#     visited = [[0]*cols for _ in range(rows)]
#     queue.append([initR, initC, cost, visited])
#     ans = float("inf")
#     while queue:
#         x, y,cost, visited = queue.popleft()
#         if (x,y) == (finalR, finalC):
#             if ans > cost:
#                 ans = cost
#         if visited[x][y] == 0:
#             new_visited = deepcopy(visited)
#             new_visited[x][y] = 1
#             for d in range(4):
#                 dx, dy = dirs[d]
#                 if -1 < x+dx< rows and -1 < y+ dy < cols:
#                     if d == 0:
#                         queue.append([x+dx,y+dy, cost+costRows[x],new_visited])
#                     elif d == 1:
#                         queue.append([x+dx,y+dy, cost+costCols[y],new_visited])
#                     elif d == 2:
#                         queue.append([x+dx, y+dy, cost+costCols[y-1],new_visited])
#                     elif d == 3:
#                         queue.append([x+dx, y+dy, cost+costRows[x-1],new_visited])
#     return ans
    

def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    # Write your code here
    cost = 0
    if initR <= finalR:
        for i in range(initR,finalR):
            cost += costRows[i]
    elif initR > finalR:
        for i in range(finalR, initR):
            cost += costRows[i-1]
    if initC <= finalC:
        for i in range(initC,finalC):
            cost += costCols[i]
    elif initC > finalC:
        for i in range(finalC, initC):
            cost += costCols[i-1]
            

    return cost

print(minCost(3,3,0,0,1,2,[2,5],[6,1]))