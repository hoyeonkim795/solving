from collections import deque

w_1 =deque([int(x) for x in input()])
w_2 =deque([int(x) for x in input()])
w_3=deque([int(x) for x in input()])
w_4=deque([int(x) for x in input()])
k=int(input())
num = []
dir = []
for _ in range(k):
    n,d = map(int,input().split())
    num.append(n)
    dir.append(d)
def rotate_r(a,b,d): #도는 주체가 a 오른쪽
    if a[2] != b[6]:
        d = -d
    else:
        d = 0
    return d #b의 d
def rotate_l(a,b,d):
    if a[6]!=b[2]:
        d=-d
    else:
        d=0
    return d

def rotate(w_1,w_2,w_3,w_4,n,d):
    # 1 > 2 > 3 > 4
    # 2 > 1,3 >4
    # 3> >2,4 >1
    # 4>3>2>1
    if n == 1:
        d_2 = rotate_r(w_1,w_2,d)
        d_3 = rotate_r(w_2,w_3,d_2)
        d_4 = rotate_r(w_3,w_4,d_3)
        w_1.rotate(d)
        w_2.rotate(d_2)
        w_3.rotate(d_3)
        w_4.rotate(d_4)
    elif n ==2:
        d_1 = rotate_l(w_2,w_1,d)
        d_3 = rotate_r(w_2,w_3,d)
        d_4 = rotate_r(w_3,w_4,d_3)
        w_2.rotate(d)
        w_1.rotate(d_1)
        w_3.rotate(d_3)
        w_4.rotate(d_4)
    elif n ==3:
        d_2 =rotate_l(w_3,w_2,d)
        d_1 =rotate_l(w_2,w_1,d_2)
        d_4=rotate_r(w_3,w_4,d)
        w_3.rotate(d)
        w_2.rotate(d_2)
        w_1.rotate(d_1)
        w_4.rotate(d_4)
    elif n==4:
        d_3= rotate_l(w_4,w_3,d)
        d_2=rotate_l(w_3,w_2,d_3)
        d_1=rotate_l(w_2,w_1,d_2)
        w_4.rotate(d)
        w_3.rotate(d_3)
        w_2.rotate(d_2)
        w_1.rotate(d_1)
    return (w_1,w_2,w_3,w_4)

        
#main
for i in range(k):
    w_1,w_2,w_3,w_4 = rotate(w_1,w_2,w_3,w_4,num[i],dir[i])

ans = 0
if w_1[0] == 1:
    ans +=1
if w_2[0] ==1:
    ans+=2
if w_3[0] ==1:
    ans+=4
if w_4[0]==1:
    ans+=8

print(ans)