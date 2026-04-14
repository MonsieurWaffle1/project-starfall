from http.client import responses
from random import choice
from random import randint
import json

from graph.commodity import *

class Building:
    def __init__(self, name, cost, buildable, type):
        self.name = name
        self.type = type

        # If a building can be constructed by the user, add the appropriate cost
        if buildable:
            self.cost = cost

        else:
            self.cost = []

        self.buildable = buildable


class Station(Building):
    def __init__(self):
        # Appears in every system, holds a system's market
        cost = {}
        self.fuel_cost = 2

        with open('config/names.json', 'r') as f:
            data = json.load(f)

        # Generates a name for the station based on a list of available options
        name = f"{choice(data["system_names"])} {choice(data["station_names"])}"
        super().__init__(name, cost, False, "station")

    def refuel(self, amount):
        return amount * self.fuel_cost


class Constructor(Building):
    def __init__(self, name, cost, buildable):
        super().__init__(name, cost, buildable, "craft")

    def produce(self, product, resources):
        return resources


class Refinery(Constructor):
    def __init__(self, level):
        # Refines ores into usable bars


        if level == "advanced":
            # Advanced level is able to create alloys
            name = "Advanced"
            cost = [
                "T3 Mechanical Components"
            ]*3

        else:
            name = "Basic"
            cost = [
                "T2 Mechanical Components"
            ]*3

        super().__init__((name+" Refinery"),cost,True)

    def produce(self, product, resources):
        for item in resources:
            if isinstance(item, Resource) and item.ore == True:
                resources.remove(item)
                item.ore = False
                resources.append(item)
                return resources

        return resources


class AdvancedRefinery(Refinery):
    def __init__(self):
        super().__init__("advanced")

    def produce(self, product, resources):
        if not isinstance(product, Alloy):
            return resources

        cost = list(product.cost)
        used = []

        for resource in resources:
            if resource in cost:
                cost.remove(resource)
                used.append(resource)

            if not cost:
                resources.append(product)

                for i in used:
                    resources.remove(i)

                break

        return resources


class BasicRefinery(Refinery):
    def __init__(self):
        super().__init__("basic")


class ManufacturingPlant(Building):
    # Used to create mechanical components
    def __init__(self):
        cost = [
            "t3_components"
        ]*5
        super().__init__("Manufacturing Plant", cost, True, "craft")

    def produce(self, tier, resources):
        count = 0
        used = []

        for resource in resources:
            if resource.tier >= tier:
                count += 1
                used.append(resource)

            if count == 3:
                for i in used:
                    resources.remove(i)

                resources.append(Component(tier))
                break

        return resources


class ResourceGen(Building):
    def __init__(self, resource):
        super().__init__(f"{resource.name} Generator", [], False, "gen")
        self.resource = resource

    def harvest(self):
        resources = []

        for i in range(randint(3,5)):
            resources.append(self.resource)

        return resources