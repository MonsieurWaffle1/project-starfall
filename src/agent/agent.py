class Agent:
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph

    def process(self, graph):
        self.graph = graph
        return self.graph