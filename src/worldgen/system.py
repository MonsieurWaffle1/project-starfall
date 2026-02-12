import random

class System:
    def __init__(self, sysID:int, layer:int) -> None:
        # Define initial system stats (placeholder)

        self.id = sysID
        self.adjacency = []
        self.sec = False
        self.tier = 1
        self.layer = layer

    def assignRandom(self, tiers:tuple):
        print(tiers)
        self.tier = random.choice(tiers)

    def assign(self,tier:int):
        self.tier = tier