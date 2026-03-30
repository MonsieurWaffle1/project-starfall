from src import Graph, Agent

class World:
    def __init__(self):
        self.graph = Graph(density=3, layers=3)
        self.agents = []

    def addAgent(self, name):
        self.agents.append(Agent(name, self.graph))

    def simulate(self):
        for agent in self.agents:
            self.graph = agent.process(self.graph)