def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x: x[1])
    print(routes)
    last_camera = routes[0][1]
    print(last_camera)
    for i in range(1,len(routes)):
        if last_camera > routes[i][0]:
            answer += 1
        last_camera = routes[i][1]

    return answer

print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, 3],[2,15]]))