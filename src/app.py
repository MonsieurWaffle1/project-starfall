from src import Agent
from world import World

if __name__ == '__main__':
    world = World()
    world.addAgent("Phil")

    cycles = int(input("How many cycles would you like?" ))

    for i in range(0,cycles):
        world.simulate()