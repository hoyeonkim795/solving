# import sys
# sys.stdin = open('input.txt', 'r')

word = input()
a = ['a','b','c','d','e','f','g','h','j','k','l','z','x','v','n','m','q','w','e','r','t','y','u','i','o','p']
b = [] # 대문자
for i in range(len(a)):
	b.append(a[i].upper())
c = list(map(str,range(0,10))) # 숫자

cnt_a = 0
cnt_b = 0
cnt_c = 0
cnt_d=0 # 특수문자
cnt_e = 0 # 비밀번호 길이
for i in range(len(word)):
    if word[i] in a:
        cnt_a += 1
    elif word[i] in b:
        cnt_b+= 1
    elif word[i] in c:
        cnt_c += 1
    else:
        cnt_d += 1

if len(word) >= 10:
    cnt_e += 1 

cnt_result = [cnt_a,cnt_b,cnt_c,cnt_d,cnt_e]

cnt = 0
for i in range(len(cnt_result)):
    if cnt_result[i] > 0:
        cnt += 1

if cnt == 1:
    result = 'LEVEL1'
elif cnt == 2:
    result = 'LEVEL2'
elif cnt == 3:
    result = 'LEVEL3'
elif cnt == 4:
    result = 'LEVEL4'
elif cnt == 5:
    result = 'LEVEL5'
print(result)

