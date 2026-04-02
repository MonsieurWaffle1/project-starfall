"""
Attribute of agent
Used to monitor cargo, fuel and modules
"""

class Ship:
    def __init__(self, capacity):
        self.cargo = []
        self.capacity = capacity
        self.used = 0

    def cargoAdd(self, item):
        # Add an item to current cargo if there is space
        temp_used = item.mass + self.used

        if temp_used > self.capacity:
            return False

        else:
            self.cargo.append(item)
            self.used += item.mass

            return True