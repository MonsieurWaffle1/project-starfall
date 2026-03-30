from src import Agent
from world import World

from graph import Graph
from src.graph.building import *

def marketTest(graph):
    my_system = True

    tier = int(input("What tier? "))

    for i in graph.systems:
        if i.tier == tier:
            my_system = i
            break

    for building in my_system.buildings:
        print(building.name)

    my_system.market.update()

    for product in my_system.market.products:
        print(f"{product.name}, {product.quantity}, {product.price}")

    while True:
        action = input(f"Buy or sell? ")
        prod = input("What product? ")
        quant = int(input("What quantity? "))

        for item in graph.commodities:
            if item.name == prod:
                prod = item
                if isinstance(prod, Resource):
                    prod.ore = False
                break

        if not isinstance(prod, str):
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

    my_system.constructBuilding(AdvancedRefinery(), [graph.components[2]] * 5)

    for building in my_system.buildings:
        print(building.name)

        if isinstance(building, ResourceGen):
            print(building.harvest())

        elif isinstance(building, Refinery):
            resource = choice(graph.resources)

            refined = building.refine(resource)

            if isinstance(building, AdvancedRefinery):
                alloy = choice(graph.alloys)
                resources = alloy.cost
                resources.append(choice(graph.resources))

                result = building.produceAlloy(alloy, resources)
                print(result)

        elif isinstance(building, ManufacturingPlant):
            resources = []
            for i in range(0,4):
                resources.append(choice(graph.alloys))

            out = building.produceComponents(resources, 2)
            print(out)

        print("")

def worldTest(graph):
    world = World()
    world.addAgent("Phil")

    cycles = int(input("How many cycles would you like?"))

    for i in range(0, cycles):
        world.simulate()



def graphTest():
    # Gets inputs from user
    my_graph = Graph(density = 3, layers = 3)

    buildingTest(my_graph)





if __name__ == '__main__':
    graphTest()