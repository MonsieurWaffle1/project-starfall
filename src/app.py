from graph import Graph
from system import System

def marketTest(graph):
    my_system = True

    tier = int(input("What tier? "))

    for i in graph.systems:
        if i.tier == tier:
            my_system = i
            break

    my_system.market.update()

    for product in my_system.market.products:
        print(f"{product.name}, {product.quantity}, {product.price}")

    while True:
        action = input(f"Buy or sell? ")
        prod = input("What product? ")
        quant = int(input("What quantity? "))

        my_system.market.adjust(action, prod, quant)
        my_system.market.update()

        print("")

        for product in my_system.market.products:
            print(f"{product.name}, {product.quantity}, {product.price}")

def buildingTest(graph):
    my_system = True

    tier = int(input("What tier? "))

    for i in graph.systems:
        if i.tier == tier:
            my_system = i
            break

    for building in my_system.buildings:
        print(building.harvest())

if __name__ == "__main__":
    # Gets inputs from user
    my_graph = Graph(density = 3, layers = 3)

    buildingTest(my_graph)



