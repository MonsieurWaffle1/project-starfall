"""
Attachments to determine the properties of each ship
"""

class Module:
    def __init__(self, name, cost):
        self.cost = cost
        self.name = name

#region Required modules
class FuelTank(Module):
    def __init__(self, capacity):
        self.capacity = capacity

        # Scales relative cost based on fuel capacity
        cost = 0
        for i in range(capacity):
            cost += 0.1


        name = f"Fuel Tank {capacity}L"
        super().__init__(name, round(cost))


class CargoHold(Module):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cargo = []
        self.used = 0

        # Scales relative cost based on cargo capacity
        cost = 0
        for i in range(capacity):
            cost += 0.015

        name = f"Cargo Bay {capacity}kg"
        super().__init__(name, round(cost))

    def add(self, item):
        # Add an item to current cargo if there is space
        temp_used = item.mass + self.used

        if temp_used > self.capacity:
            return False

        else:
            self.cargo.append(item)
            self.used += item.mass

            return True
#endregion

#region Hardpoint modules
class Hardpoint(Module):
    def __init__(self, name, cost, dmg):
        self.dmg = dmg
        super().__init__(name, cost)


class MiningBeam(Hardpoint):
    def __init__(self, capacity):
        name = "T1 Mining Beam"
        cost = 3

        super().__init__(name, cost, 5)
#endregion