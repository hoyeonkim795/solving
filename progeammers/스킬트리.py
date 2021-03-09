from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skills = deque(list(skill))
        skill_tree = list(skill_tree)
        order = deque()
        for tree in skill_tree:
            if tree in skills:
                order.append(tree)
        # print(order)
        while order:
            a = order.popleft()
            b = skills.popleft()
            if a != b:
                break
        else:
            answer += 1 
        # print(answer)


    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))