"""
Class to represent the market state of a system, and updates commodity prices based on supply and demand.
Uses different price calculations dependent on what the system is producing.
"""

from commodity import Resource

class MarketItem:
    def __init__(self, item, name, quantity, price):
        self.object = item
        self.name = name
        self.quantity = quantity
        self.price = price

class Market:
    def __init__(self, commodities):
        self.products = []
        self.commodities = commodities

    def priceCalc(self, item, Q):
        # If no subclass is used, return to fallback equation
        return round(90 / (1 + (Q / 45)))

    def update(self):
        # Adjust price of each product based on the relevant equation
        for product in self.products:
            product.price = self.priceCalc(product, product.quantity)

    def adjust(self, action, item, Q):
        # Performs buy and sell ops

        # Clean data and sets a flag to check if the resource exists
        exists = False
        action = action.lower()

        # Finds the item
        for i in self.products:
            if i.name.lower() == item.name.lower():
                exists = True
                item = i
                break

        if not exists:
            if action == "sell":
                return self.add(item, Q)

            else:
                return False

        # Performs the relevant buy/sell action
        if action == "buy":
            if item.quantity < Q:
                return False

            item.quantity -= Q
            return True

        elif action == "sell":
            item.quantity += Q
            return True

        else:
            return False

    def add(self, item, Q):

        if isinstance(item, Resource):
            if item.ore:
                return False

        component = MarketItem(item, item.name, Q, 0)
        self.products.append(component)

        return True


class MiningMarket(Market):
    def __init__(self, main, commodities):
        super().__init__(commodities)
        self.main = main

    def priceCalc(self, item, Q):
        # Use different equations depending on how abundant the resource is in the system
        modifier = 1

        for resource in self.main:
            if resource.name.lower() == item.name.lower():
                modifier = 0.8
                break

        if item.object.tier == 2:
            modifier = 1.7

        elif item.object.tier == 3:
            modifier = 1.9

        elif item.object.tier == 4:
            modifier = 2.5


        return round((100 / (1 + (Q / 30))) * modifier)


class ManufacturingMarket(Market):
    def __init__(self, tier, commodities):
        super().__init__(commodities)
        self.tier = tier

    def priceCalc(self, item, Q):
        modifier = 1

        if self.tier == 2:
            if item.object.tier == 1:
                modifier = 1.2

            elif item.object.tier == 2:
                modifier = 1.4

            elif item.object.tier == 3:
                modifier = 1.8

            elif item.object.tier == 4:
                modifier = 2.2

            return round((120 / (1 + (Q / 45))) * modifier)


        # Use different equation depending on what level of resource is being manufactured in the system
        else:
            if item.object.tier == 1:
                modifier = 1

            elif item.object.tier == 2:
                modifier = 1.2

            elif item.object.tier == 3:
                modifier = 1.6

            elif item.object.tier == 4:
                modifier = 1.8


            return round((110 / (1 + (Q / 55))) * modifier)
