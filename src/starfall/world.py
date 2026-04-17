from starfall import Graph, Agent

class World:
    def __init__(self, density, layers):
        self.graph = Graph(density, layers)
        self.agents = []

    def addAgent(self, name):
        # Use when you want a random agent type
        self.agents.append(Agent(name, self.graph))

    def addSpecificAgent(self, agent):
        # Use to force a specific agent type
        self.agents.append(agent)

    def simulate(self):
        for agent in self.agents:
            print(f"Simulating {agent.name}")
            self.graph = agent.process(self.graph)