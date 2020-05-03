from collections import deque

result = 27
ans = deque()     
while result > 0:
    if result%2 == 1:
        ans.appendleft('1')
        result //= 2
        print(result)
    else:
        ans.appendleft('0')
        result //=2
        print(result)

print(ans)

    