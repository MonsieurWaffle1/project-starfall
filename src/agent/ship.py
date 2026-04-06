"""
Attribute of agent
Used to monitor cargo, fuel and modules
"""

from agent.module import *

class Ship:
    def __init__(self, fuel, cargo):
        # Add a fuel tank and cargo hold based on requirements
        self.tank = FuelTank(fuel)
        self.cargo_hold = CargoHold(cargo)

        # If hardpoints do not exist, create a template
        if not "self.hardpoints" in locals():
            self.hardpoints = {
                0:None,
                1:None
            }

    def cargoAdd(self, item):
        return self.cargo_hold.add(item)

#region Ship classes
class Miner(Ship):
    def __init__(self):
        self.hardpoints = {
            0:MiningBeam,
            1:None,
            2:None
        }

        super().__init__(15, 150)

class Explorer(Ship):
    def __init__(self):
        self.hardpoints = {
            0:None,
            1:None
        }

        super().__init__(25, 100)
#endregion