class Commodity:
    def __init__(self, name, tier):
        self.name: str = name
        self.tier: int = tier

class Resource(Commodity):
    def __init__(self, name):
        super().__init__(name, 1)

class Alloy(Commodity):
    def __init__(self, name, cost, tier):
        super().__init__(name, tier)
        self.cost: tuple = cost

class Component(Commodity):
    def __init__(self, tier):
        super().__init__(f"T{tier} Mechanical Components", tier)