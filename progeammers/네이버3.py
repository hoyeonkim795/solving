num_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
num_pair = [0]*len(num_list)
for i in range(len(num_list)):
    num_pair[i] = (i,num_list[i])
num_pair = sorted(num_pair, key=lambda x: x[1])
include = [False]*len(num_list)
print(num_pair)
k = 11
# 전체에서 - 첫자리가 0인경우
ans = 0
def create_num(weight,num):
    global ans
    if weight <= k and not num.startswith('0'):
        if weight == k:
            ans += 1
            print(num)
            return
        else:
            for j in range(len(num_pair)):
                create_num(weight+num_pair[j][1], num + str(num_pair[j][0]))
            
print(create_num(0,''))
if k == 6:
    ans += 1
print(ans)