from system import system
from random import randint

'''
A graph class that builds itself into the world map.
Systems are created and filled out with attributes according to user input.
'''

class Graph:
    def __init__(self, density: int, layers: int) -> None:
        # Instantiates variables
        self.id_count: int = 1
        self.systems: list = []
        self.density: int = density
        self.layers: int = layers

        # Runs setup function
        self.setup()


    def setup(self) -> None:
        # Function to generate the world

        start_node = system(self.id_count,0)
        self.systems.append(start_node)

        self.systemGen(start_node,1)

        pass


    def systemGen(self, source, layer) -> None:
        # Recursive function to create systems according to layers and density

        if layer > self.layers:
            # Breaks out if layer limit has been reached
            return

        for i in range(self.density):
            # A new system is created and added to the node list
            self.id_count += 1
            node = system(self.id_count,layer)

            # Relevant adjacencies are are added
            distance = randint(2,12)
            node.adjacency.append({"target" : source.id,
                                   "distance" : distance})
            source.adjacency.append({"target" : node.id,
                                     "distance" : distance})

            # Adds the new node to the list and recurs
            self.systems.append(node)
            self.systemGen(node,layer+1)


if __name__ == "__main__":
    # Gets inputs from user
    my_graph = Graph(density = 2, layers = 4)

    if my_graph.systems[1].id != my_graph.systems[2].id:
        print("yay!")