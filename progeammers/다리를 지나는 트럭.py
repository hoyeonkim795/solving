from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = deque(truck_weights)
    ans = len(truck_weights)
    moving = deque()
    state = deque()
    done = []
    while len(done) != ans:
        for i in range(len(state)):
            state[i] += 1
        
        if len(truck_weights) > 0: 
            truck = truck_weights.popleft()
            if sum(moving) + truck <= weight:
                moving.append(truck)
                state.append(1)
            else:
                truck_weights.appendleft(truck)
        answer += 1
        while True:
            if len(state) == 0:
                break
            if state[0] == bridge_length:
                state.popleft()
                b = moving.popleft()
                done.append(b)
            elif state[0] < bridge_length:
                break
        # print(answer, done)
        
            
    return answer


print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))