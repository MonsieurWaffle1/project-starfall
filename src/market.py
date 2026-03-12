"""
Class to represent the market state of a system, and updates commodity prices based on supply and demand.
Uses different price calculations dependent on what the system is producing.
"""

class MarketItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Market:
    def __init__(self):
        self.products = []

    def priceCalc(self, item, Q):
        # If no subclass is used, return to fallback equation
        return round(90 / (1 + (Q / 45)))

    def update(self):
        for product in self.products:
            product.price = self.priceCalc(product.name, product.quantity)

    def adjust(self, action, item, Q):
        exists = False
        action = action.lower()
        item = item.lower()

        for i in self.products:
            if i.name == item:
                exists = True
                item = i
                break

        if not exists:
            return False

        if action == "buy":
            return self.buy(item, Q)

        elif action == "sell":
            return self.sell(item, Q)

        else:
            return False

    def buy(self, item, Q):
        if item.quantity < Q:
            return False

        item.quantity -= Q
        return True


    def sell(self, item, Q):
        item.quantity += Q
        return True


class MiningMarket(Market):
    def __init__(self, main):
        super().__init__()
        self.main = main

    def priceCalc(self, item, Q):
        # Use different equations depending on how abundant the resource is in the system
        if item in self.main:
            return round(100 / (1 + (Q / 80)))

        else:
            return round(80 / (1 + (Q / 30)))


class ManufacturingMarket(Market):
    def __init__(self, tier):
        super().__init__()
        self.tier = tier

    def priceCalc(self, item, Q):
        # Use different equation depending on what level of resource is being manufactured in the system
        if self.tier == 3:
            return round(110 / (1 + (Q / 35)))

        else:
            return round(120 / (1 + (Q / 40)))