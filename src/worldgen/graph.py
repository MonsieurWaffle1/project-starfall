from system import System
from random import randint

'''
A graph class that builds itself into the world map.
Systems are created and filled out with attributes according to user input.
'''

class Graph:
    def __init__(self, density: int, layers: int) -> None:
        # Instantiates variables
        self.transition_points = {
            "1":0,
            "2":0
        }
        self.id_count: int = 1
        self.systems: list = []
        self.density: int = density
        self.layers: int = layers

        # Runs setup function
        self.setup()


    def setup(self) -> None:
        # Function to generate the world

        start_node = System(self.id_count, 0)
        self.systems.append(start_node)

        self.systemGen(start_node,1)

        self.tierAssign()

        pass


    def systemGen(self, source, layer) -> None:
        # Recursive function to create systems according to layers and density

        if layer > self.layers:
            # Breaks out if layer limit has been reached
            return

        for i in range(self.density):
            # A new system is created and added to the node list
            self.id_count += 1
            node = System(self.id_count, layer)

            # Relevant adjacencies are are added
            distance = randint(2,12)
            node.adjacency.append({"target" : source.id,
                                   "distance" : distance})
            source.adjacency.append({"target" : node.id,
                                     "distance" : distance})

            # Adds the new node to the list and recurs
            self.systems.append(node)
            self.systemGen(node,layer+1)


    def tierAssign(self):
        # Determine transition points
        interval = self.layers//3
        layer = 0

        for i in range(1,3):
            layer += interval
            self.transition_points[str(i)] = layer

        for sys in self.systems:
            # Uses separate function if a transition point

            if sys.layer in self.transition_points.values():
                # Passes the correct tuple based on transition point
                if self.transition_points["1"] == sys.layer:
                    tiers = (2,3)
                else:
                    tiers = (1,2)

                sys.assignRandom(tiers)

            # Assigns tier based on layer
            elif self.transition_points["1"] > sys.layer:
                sys.assign(3)

            elif self.transition_points["2"] < sys.layer:
                sys.assign(1)

            else:
                sys.assign(2)




if __name__ == "__main__":
    # Gets inputs from user
    my_graph = Graph(density = 2, layers = 4)

    for system in my_graph.systems:
        print(system.layer)