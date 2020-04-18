tc = int(input())
def calculate(a,b,op):
    if op == '+':
        return a+b
    if op == '-':
        return a-b
    if op == '/':
        return  int(a/b)
    if op =='*':
        return int(a*b)
def eq(num_info,op_info):
    s = num_info[0]
    for i in range(len(num_info)-1):
        s = int(calculate(s,num_info[i+1],op_info[i]))
        #print(s)
    result = s
    return result

def permutation(arr,r):

    used = [0 for _ in range(len(arr))]
    def generate(chosen, used):
        if len(chosen) == r:
            print(num_info,chosen)
            final = eq(num_info,chosen)
            print(final)
            return final

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen,used)
                used[i] = 0
    generate([],used)


for tc in range(tc):
    N = int(input())
    info = list(map(int,input().split()))
    num_info = list(map(int,input().split()))
    op_info = []
    for i in range(info[0]):
        op_info.append('+')
    for i in range(info[1]):
        op_info.append('-')
    for i in range(info[2]):
        op_info.append('*')
    for i in range(info[3]):
        op_info.append('/')

    print(permutation(op_info,len(op_info)))






