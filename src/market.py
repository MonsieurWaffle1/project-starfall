"""
Class to represent the market state of a system, and updates commodity prices based on supply and demand.
Uses different price calculations dependent on what the system is producing.
"""

class Market:
    def __init__(self):
        self.products = {}

    def priceCalc(self, item, Q):
        # If no subclass is used, return to fallback equation
        return (100 - Q) / 1.0


class MiningMarket(Market):
    def __init__(self, main):
        super().__init__()
        self.main = main

    def priceCalc(self, item, Q):
        # Use different equations depending on how abundant the resource is in the system
        if item == self.main:
            return (200 - Q) / 0.8

        else:
            return (80 - Q) / 1.2


class ManufacturingMarket(Market):
    def __init__(self, tier):
        super().__init__()
        self.tier = tier

    def priceCalc(self, item, Q):
        # Use different equation depending on what level of resource is being manufactured in the system
        if self.tier == 3:
            return (120 - Q) / 1.3

        else:
            return (120 - Q) / 1.5