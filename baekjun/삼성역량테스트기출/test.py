from typing import List, Text


class NoAgentFoundException(Exception):
    pass

class Agent(object):
    def __str__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load
        self._name = []
        self._name.append(self.name)
        self._name.append(self.skills)
        self._name.append(self.load)

        return "<Agent: {}>".format(self._name)
class Ticket(object):
    def __str__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions
        self._ticket = []
        self._ticket.append(self.id)
        self._ticket.append(self.restrictions)
        return "<Ticket: {}>".format(self._ticket)

ticket = Ticket(id="1", restrictions=["Engilish"])
agent1 = Agent(name='john',skills ='english',load =1)
agent2 = Agent(name='hy',skills ='english',load =0)

class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        self.ticket = ticket
        self.agents = agents
        now_min = int(agents[0][3])
        for i in range(len(agents)):
            if int(agents[i][3]) <= now_min:
                self._leastload = agents[i][0]

        return self._leastload

a = LeastLoadedAgent(id="1", restrictions=["Engilish"])
ticket = Ticket(id="1", restrictions=["Engilish"])
print(a.find(ticket,[agent1,agent2]))

# a = Agent()
# print(a.__str__(name = 'john',skills = 'english',load =1))
# from typing import List
# Vector = List[float]

# def scale(scalar: float, vector: Vector) -> Vector:
#     return [scalar * num for num in vector]

# # 형 검사 통과; float의 리스트는 Vector로 적합합니다.
# new_vector = scale(2.0, [1.0, -4.2, 5.4])
# print(new_vector)