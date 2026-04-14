"""
App to facilitate function tests
"""
#region Dependencies
from agent.agent import AgentTravelTest
from world import World

from graph import Graph
from src.graph.building import *

from random import choice
#endregion

#region Graph testing
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

            if isinstance(building, AdvancedRefinery):
                alloy = choice(graph.alloys)
                resources = alloy.cost
                resources.append(choice(graph.resources))

                result = building.produce(alloy, resources)
                print(result)

        elif isinstance(building, ManufacturingPlant):
            resources = []
            for i in range(0,4):
                resources.append(choice(graph.alloys))

            out = building.produce(resources, 2)
            print(out)

        print("")

def genTest(graph):
    for i in range(1,3):
        # Print adjacencies for a random system
        system = choice(graph.systems)
        for adj in system.adjacency:
            print(f"System ID: {adj["system"].id}")
            print(f"Distance: {adj["distance"]}")

    # Print T1 resources
    for system in graph.systems:
        if system.tier == 1:
            for resource in system.resources:
                print(resource.name)
            break
#endregion

#region World tests
def travelTest(world):
    world.addSpecificAgent(AgentTravelTest("Explorer Agent", world.graph))

    for i in range(0, 5):
        world.simulate()
        my_agent = world.agents[0]
        print(my_agent.system.id)
#endregion

#region Agent tests
def refuelTest(world):
    agent = world.agents[0]

    agent.ship.tank.fuel_level -= 10

    print(agent.refuel(10))


def buyTest(world):
    agent = world.agents[0]
    market = agent.system.market

    item = market.products[0].object

    print(agent.buy(item, 1))

def sellTest(world):
    agent = world.agents[0]
    market = agent.system.market

    item = market.products[0].object
    agent.ship.cargo_hold.cargo.append(item)
    agent.ship.cargo_hold.used += item.mass

    print(agent.sell(item, 1))

def mineTest(world):
    agent = world.agents[0]
    print(agent.mine())

def produceTest(world):
    agent = world.agents[0]
    market = agent.system.market
    item = market.products[0].object
    item.ore = True

    agent.ship.cargo_hold.cargo.append(item)
    agent.ship.cargo_hold.used += item.mass

    agent.system.constructBuilding(BasicRefinery(), [world.graph.components[1]] * 3)

    print(agent.produce("refine"))




#endregion

def worldTest():
    world = World(3, 3)

    print("[1] General test")
    print("[2] Travel test")

    test = input("What type? ")

    if test == "1":
        cycles = int(input("How many cycles would you like?"))
        world.addAgent("James")
        world.addAgent("Fred")
        for i in range(0, cycles):
            world.simulate()

    elif test == "2":
        travelTest(world)

def graphTest():
    # Gets inputs from user
    my_graph = Graph(density = 3, layers = 3)

    print("What test?")
    print("[1] Market")
    print("[2] Building")
    print("[3] Generation")
    i = input()

    if i == "1":
        marketTest(my_graph)

    elif i == "2":
        buildingTest(my_graph)

    elif i == "3":
        genTest(my_graph)

def agentTest():
    world = World(3, 3)
    world.addAgent("James")
    world.agents[0].money += 100000

    for system in world.graph.systems:
        if system.tier == 1:
            world.agents[0].system = system
            break

    print("What test?")
    print("[1] Refuel")
    print("[2] Buy")
    print("[3] Sell")
    print("[4] Mine")
    print("[5] Produce")
    i = input()
    if i == "1":
        print (True)
        return True
        refuelTest(world)

    elif i == "2":
        buyTest(world)

    elif i == "3":
        sellTest(world)

    elif i == "4":
        mineTest(world)

    elif i == "5":
        produceTest(world)

if __name__ == '__main__':
    print("What test?")
    print("[1] Graph")
    print("[2] World")
    print("[3] Agent")
    i = input()

    if i == "1":
        graphTest()

    elif i == "2":
        worldTest()

    elif i == "3":
        agentTest()