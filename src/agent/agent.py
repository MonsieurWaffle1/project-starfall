from random import choice
from random import randint

from agent.ship import *



class Agent:
    def __init__(self, name, graph):
        # Initializes variables and sets random location
        self.name = name
        self.graph = graph
        self.system = choice(graph.systems)
        self.adjacencies = self.system.adjacency
        self.ship = Miner()

        self.money = 100

    def travel(self, target):
        # Function to allow an agent to travel between systems

        # Finds target system
        found = False
        distance = 0

        for i in self.adjacencies:
            if i["system"].id == target:
                target = i["system"]
                distance = i["distance"]
                found = True

        # If system is adjacent, set new location
        if not found:
            return False

        # Checks if ship has enough fuel
        #elif self.ship.tank.fuel_level < distance:
        #    return False

        else:
            self.system = target
            self.adjacencies = self.system.adjacency
            self.ship.tank.fuel_level -= distance
            return True

    def refuel(self, quantity):
        # Refuels the ship. Fails if can't afford
        station = None
        for building in self.system.buildings:
            if building.type == "station":
                station = building
                break

        cost = station.refuel(quantity)

        if cost < self.money:
            self.money -= cost
            self.ship.tank.fuel_level += quantity
            return True

        else:
            return False

    def buy(self, product, quantity):
        market = self.system.market

        found = False
        cost = 0
        market_item = None

        # Finds the wanted item in the system's market
        for item in market.products:
            if item.object == product:
                market_item = item
                found = True

                cost = item.price * quantity

        # Fails if the item does not exist
        if not found:
            return False

        # Checks if the agent can afford the item
        elif self.money < cost:
            return False

        elif market_item.quantity < quantity:
            return False

        # Checks if the agent has the needed storage space
        elif product.mass * quantity > self.ship.cargo_hold.capacity - self.ship.cargo_hold.used:
            return False

        else:
            # Buys item and adds to inventory
            self.money -= cost
            market_item.quantity -= quantity
            self.ship.cargo_hold.used += product.mass * quantity

            for i in range(0, quantity):
                self.ship.cargo_hold.cargo.append(product)

            # Adjusts market conditions
            return market.adjust("buy", product, quantity)

    def sell(self, product, quantity):
        market = self.system.market

        found = False
        cost = 0
        market_item = None

        # Determines how many of the resource the agent has
        quant = 0
        for item in self.ship.cargo_hold.cargo:
            if item == product:
                quant += 1

        # Finds the item in the market
        for item in market.products:
            if item.object == product:
                market_item = item
                found = True

                cost = item.price * quantity

        # Checks if the item exists
        if not found:
            return False

        # Checks if the agent has the required quantity
        elif quantity > quant:
            return False

        else:
            # Pay the agent and add product to the market
            self.money += cost
            self.system.market.adjust("sell", product, quantity)

            # Removes the items from the ship's inventory
            for item in self.ship.cargo_hold.cargo:
                if quant == 0:
                    break

                elif item == product:
                    self.ship.cargo_hold.cargo.remove(product)
                    quant -= 1

            return True

    def mine(self):
        gen = False
        mining_tool = False
        building = None

        # Finds a building with the "gen" attribute
        for building in self.system.buildings:
            if building.type == "gen":
                gen = True
                break

        # Finds a mining-equipped hardpoint
        for tool in self.ship.hardpoints.values():
            if tool is None:
                pass
            elif tool.mining:
                mining_tool = True
                break

        # Checks a gen building has been found
        if not gen:
            return False

        # Checks if the agent's ship has a mining tool
        if not mining_tool:
            return False

        else:
            produced = building.harvest()

            for resource in produced:
                # Checks the cargo capacity will not be exceeded
                if self.ship.cargo_hold.used + resource.mass <= self.ship.cargo_hold.capacity:
                    # Adds the resource to the cargo hold
                    self.ship.cargo_hold.used += resource.mass
                    self.ship.cargo_hold.cargo.append(resource)

            return True

    def produce(self, product):
        craft = False
        building = None

        # Identifies a building with the "craft" attribute
        for building in self.system.buildings:
            if building.type == "craft":
                craft = True
                break

        # Checks a craft building has been found
        if not craft:
            return False

        # Performs the production and creates a new cargo list
        new_cargo = building.produce(product, self.ship.cargo_hold.cargo)

        # Calculates mass of new cargo
        new_mass = 0
        for product in new_cargo:
            new_mass += product.mass

        # Checks the mass limit will not be exceeded
        if new_mass > self.ship.cargo_hold.capacity:
            return False

        # Updates the resource and capacity variables
        else:
            self.ship.cargo_hold.used = new_mass
            self.ship.cargo_hold.cargo = new_cargo
            return True

    def process(self, graph):
        return self.graph


#region Testing subclasses
class AgentTravelTest(Agent):
    def __init__(self, name, graph):
        super().__init__(name, graph)
        self.ship = Explorer()

    def process(self, graph):
        self.graph = graph

        # Travels to a random adjacent system
        index = randint(0, len(self.adjacencies) - 1)
        id = self.adjacencies[index]["system"].id
        self.travel(id)

        return self.graph
#endregion