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


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        self.ticket = ticket
        self.agents = agents
        self._leastload = ''
        now_min = int(agents[0][3])
        for i in range(len(agents)):
            if int(agents[i][3]) <= now_min:
                self._leastload = agents[i][0]

        raise NotImplemented
        return self._leastload


# class LeastFlexibleAgent(FinderPolicy):
#     def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
#         self.ticket = ticket
#         self.agents = agents
#         self.flexible_agent = ''
#         if self.ticket[1] in self.agents[1]:
#             if len(self.agents[1]) == 1

#         raise NotImplemented


ticket = Ticket(id="1", restrictions=["Engilish"])
agent1 = Agent(name='john',skills ='english',load =1)
agent2 = Agent(name='hy',skills ='english',load =0)
