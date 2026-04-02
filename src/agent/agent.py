from random import choice
from random import randint

from ship import Ship

class Agent:
    def __init__(self, name, graph):
        # Initializes variables and sets random location
        self.name = name
        self.graph = graph
        self.system = choice(graph.systems)
        self.adjacencies = self.system.adjacency
        self.ship = Ship(80)

    def travel(self, target):
        # Function to allow an agent to travel between systems

        # Finds target system
        found = False
        for i in self.adjacencies:
            if i["system"].id == target:
                target = i["system"]
                found = True

        # If system is adjacent, set new location
        if not found:
            return False

        else:
            self.system = target
            self.adjacencies = self.system.adjacency
            return True


    def process(self, graph):
        return self.graph


#region Testing subclasses
class AgentTravelTest(Agent):
    def __init__(self, name, graph):
        super().__init__(name, graph)

    def process(self, graph):
        self.graph = graph

        # Travels to a random adjacent system
        index = randint(0, len(self.adjacencies) - 1)
        id = self.adjacencies[index]["system"].id
        self.travel(id)

        return self.graph
#endregion