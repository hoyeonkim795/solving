p = "()))((()"

def check(p):
    q = []
    for i in range(len(p)):
        if len(q) > 0 and p[i] == ')':
            q.pop()
        else:
            q.append(p[i])
    return len(q)
def find(p):
    for i in range(2,len(p)): #2
        if p[:i].count('(') == p[:i].count(')') and p[i:].count('(') == p[i:].count(')'):
                return i

def solution(p):
    if p == '' or check(p)==0: #1
        return p
    else:
        i = find(p)
        u, v = p[:i],p[i:]
        if check(u) == 0: #3
            answer = solution(v)
            return u + answer
        else:
            string = '('
            string += solution(v)
            string += ')'
            new_u = ''
            for i in range(1,len(u)-1):
                if u[i] == '(':
                    new_u += ')'
                else:
                    new_u += '('
            string += new_u
            return string

print(solution(p))