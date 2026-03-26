import random
from building import *

class System:
    def __init__(self, sysID:int, layer:int) -> None:
        # Define initial system stats (placeholder)

        self.id = sysID
        self.adjacency = []
        self.sec = True
        self.tier = 1
        self.layer = layer
        self.resources = []
        self.buildings = []

    def assignRandom(self, tiers:tuple):
        self.tier = random.choice(tiers)
        self.secAssign()


    def assign(self,tier:int):
        self.tier = tier
        self.secAssign()

    def secAssign(self):
        # Changes to low sec if T1 system
        if self.tier == 1:
            self.sec = False

    def constructBuilding(self, building:Building, resources):
        if not building.buildable:
            return resources

        cost = building.cost
        used = []

        for resource in resources:
            for i in cost:
                if resource.name == i:
                    cost.remove(resource.name)
                    used.append(resource)

                if not cost:
                    self.buildings.append(building)

                    for i in used:
                        resources.remove(i)

                    break

        return resources