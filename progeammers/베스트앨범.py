genres = ['classic','pop','classic','pop','classic','classic']
plays = [400,600,150,2500,500,500]
def solution(genres, plays):
    answer = []
    dic = dict()
    genre = dict()
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [[i,plays[i]]]
        else:
            dic[genres[i]].append([i,plays[i]])
        if genres[i] not in genre:
            genre[genres[i]] = plays[i]
        else:
            genre[genres[i]] += plays[i]

    for key,value in dic.items():
        dic[key] = sorted(dic[key], key= lambda x: x[1] -x[0], reverse=True)

    genre = sorted(genre.items(), key=lambda x: x[1], reverse=True)
    print(dic)
    for i in genre:
        if len(dic[i[0]]) > 1:
            answer.append(dic[i[0]][0][0])
            answer.append(dic[i[0]][1][0])
        elif len(dic[i[0]]) == 1:
            answer.append(dic[i[0]][0][0])
    

    return answer

print(solution(genres,plays))