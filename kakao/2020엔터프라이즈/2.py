import sys
sys.stdin = open('input.txt', 'r')
import collections
n = int(input())
score = dict()
b_score = dict() 

for i in range(n*(n-1)):
    t1,s1,t2,s2 = input().split()

    if int(s1) > int(s2):
        if t1 not in score.keys():
            score[t1] = 1
        else:
            score[t1] += 1
        if t2 not in score.keys(): # t2 의 패배
            score[t2] = 0
        #득수 구하기
        if t2 not in b_score.keys():
            b_score[t2] = int(s2)-int(s1)
        else:
            b_score[t2] += int(s2)-int(s1)
        if t1 not in b_score.keys():
            b_score[t1] = int(s1)-int(s2)
        else:
            b_score[t1] += int(s1)-int(s2)

        
        # 세트 득실       

    else:
        if t2 not in score.keys():
            score[t2] = 1
        else:
            score[t2] += 1
        if t1 not in score.keys():
            score[t1] =0
        # 득수 구하기
        if t2 not in b_score.keys():
            b_score[t2] = int(s2)-int(s1)
        else:
            b_score[t2] += int(s2)-int(s1)
        if t1 not in b_score.keys():
            b_score[t1] = int(s1)-int(s2)
        else:
            b_score[t1] += int(s1)-int(s2)

final = []
for i in score_sort.keys():
    final.append([i,score_sort[i],b_score[i]])
for i in range(1,len(final)):
    if final[i][1] == final[i-1][1]: # 승수가 같으면
        if final[i][2] > final[i-1][2]: # 세트수와 큰것과 교한
            final[i],final[i-1] = final[i-1],final[i]
        elif final[i][2] == final[i-1][2]: # 세트수가 같으면
            if ord(final[i][0][0]) < ord(final[i-1][0][0]):
                final[i],final[i-1] = final[i-1],final[i]


for i in range(len(final)):
    print(' '.join(map(str,final[i])))


