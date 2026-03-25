from random import choice
from random import randint
import json

from commodity import *

class Building:
    def __init__(self, name, cost, buildable):
        self.name = name

        # If a building can be constructed by the user, add the appropriate cost
        if buildable:
            self.cost = cost

        else:
            self.cost = {}



class Station(Building):
    def __init__(self):
        # Appears in every system, holds a system's market
        cost = {}
        system_names = []
        station_names = []

        with open('config/names.json', 'r') as f:
            data = json.load(f)

        # Generates a name for the station based on a list of available options
        name = f"{choice(data["system_names"])} {choice(data["station_names"])}"
        super().__init__(name, cost, False)


class Refinery(Building):
    def __init__(self, level):
        # Refines ores into usable bars


        if level == "advanced":
            # Advanced level is able to create alloys
            name = "Advanced"
            cost = {
                "t3_components":3
            }

        else:
            name = "Basic"
            cost = {
                "t2_components":3
            }

        super().__init__((name+" Refinery"),cost,True)

    def refine(self, item):
        if isinstance(item, Resource) and item.ore == True:
            item.ore = False

        return item


class AdvancedRefinery(Refinery):
    def __init__(self):
        super().__init__("advanced")


class BasicRefinery(Refinery):
    def __init__(self):
        super().__init__("basic")


class ManufacturingPlant(Building):
    # Used to create mechanical components
    def __init__(self):
        cost = {
            "t3_components":5
        }
        super().__init__("Manufacturing Plant", cost, True)


class ResourceGen(Building):
    def __init__(self, resource):
        super().__init__(f"{resource.name} Generator", [], False)
        self.resource = resource

    def harvest(self):
        return self.resource, randint(3,5)