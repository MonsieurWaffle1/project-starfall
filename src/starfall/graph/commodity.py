class Commodity:
    def __init__(self, name, tier, mass):
        self.name: str = name
        self.tier: int = tier
        self.mass = mass

class Resource(Commodity):
    def __init__(self, name, mass):
        super().__init__(name, 1, mass)
        self.ore = True

class Alloy(Commodity):
    def __init__(self, name, cost, tier, mass):
        super().__init__(name, tier, mass)
        self.cost: tuple = cost

class Component(Commodity):
    def __init__(self, tier, mass):
        super().__init__(f"T{tier} Mechanical Components", 4, mass)