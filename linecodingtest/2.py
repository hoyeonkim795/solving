# 부정행위 가능성 지수 = 총 의심 문항의 수 + (가장 긴 연속된 의심 문항의 수)2
answer_sheet = "4132315142"
sheets = ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]

def find_longest(bad):
    longest_max = 0

    for i in range(len(bad)):
        c_max = 0
        for j in range(i,len(bad)):
            if bad[i]==1 and bad[i] == bad[j]:
                c_max +=1
            else:
                break
        if c_max> longest_max:
            longest_max = c_max
    return longest_max

def solution(answer_sheet, sheets):
    answer = 0 #부정행위 가능 지수
    incorrect = [[0]*len(answer_sheet) for _ in range(len(sheets))]

    for i in range(len(answer_sheet)):
        # 오답인 문항 찾기
        for j in range(len(sheets)):
            if answer_sheet[i] != sheets[j][i]:
                incorrect[j][i] = -1  #틀린거 표시
    
    
    max_arr = []
    for i in range(len(incorrect)-1): #사람수
        longest_max = 0 #가장 긴 의심문항수

        for k in range(i+1,len(incorrect)): # 다른사람과 비교하기
            bad = [0]*len(answer_sheet) #의심문항의 수

            for j in range(len(answer_sheet)): # 문항수
                
                if incorrect[i][j] == -1 and incorrect[k][j]== -1 and sheets[i][j] == sheets[k][j]:
                    bad[j] = 1
        
        # longest 조사하기
            count_1 = bad.count(1)

            max_arr.append(count_1 +(find_longest(bad))**2)
    answer = max(max_arr)
        

        


    return answer

print(solution(answer_sheet, sheets))