
import sys
sys.stdin = open("input.txt",'r')
info = list(map(int,input().split()))
print(info)
board = [[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0],[10,13,16,19,25],[20,22,24,25],[30,28,27,26,25],[25,30,35,40]]

horse = [[0,0],[0,0],[0,0],[0,0]]

# 브루트포스
for i in range(info):
    for j in range(4):
        choosen_horse = horse[j] # 4개중에 하나를 고름
        if 4 < choosen_horse[1] + info[i]:
            
            new_horse = [4,choosen_horse[0][1] + info[i]-4]
            if new_horse not in hotse:
                horse[j] = new_horse