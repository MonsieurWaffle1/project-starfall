import random
from market import Market

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
        self.market = Market()

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
