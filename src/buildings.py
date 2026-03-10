from names import system_names
from names import station_names

from random import choice

class Building:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Refinery(Building):
    def __init__(self, level):
        if level == "advanced":
            name = "Advanced"
            cost = {
                "t3_components":3
            }

        else:
            name = "Basic"
            cost = {
                "t2_components":3
            }

        super().__init__(name=(name+" Refinery"), cost = cost)


class AdvancedRefinery(Refinery):
    def __init__(self):
        super().__init__("advanced")


class BasicRefinery(Refinery):
    def __init__(self):
        super().__init__("basic")


class ManufacturingPlant(Building):
    def __init__(self):
        cost = {
            "t3_components":5
        }
        super().__init__("Manufacturing Plant", cost)