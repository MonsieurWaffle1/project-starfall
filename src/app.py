from src.graph import Graph



if __name__ == "__main__":
    # Gets inputs from user
    my_graph = Graph(density = 2, layers = 4)

    for building in my_graph.buildings:
        print(building)