import sys
sys.stdin=open('input.txt','r')
from itertools import combinations
from collections import deque
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
people = [int(x) for x in range(n)]
com_people = list(combinations(people,n//2))
final_com = deque()
ans = deque()
for i in range(len(com_people)//2):
    course = list(com_people[i]+com_people[-i-1])
    final_com.append(course)
    start = 0
    link = 0
    for j in range(len(final_com[i])//2):
        for k in range(len(final_com[i])//2):
            start += board[final_com[i][j]][final_com[i][k]]
            link += board[final_com[i][-j-1]][final_com[i][-k-1]]
    ans.append(abs(start-link))
ans = set(ans)
print(min(ans))    
        

    