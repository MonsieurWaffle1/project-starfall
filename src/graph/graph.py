from graph.system import System
from graph.building import *
from graph.market import *
from graph.commodity import *

from random import randint
from random import sample
from random import choice
import json


'''
A graph class that builds itself into the world map.
Systems are created and filled out with attributes according to user input.
'''

class Graph:
    def __init__(self, density: int, layers: int) -> None:
        # Instantiates variables
        self.transition_points = {
            "1":0,
            "2":0
        }

        self.id_count: int = 1
        self.systems: list = []
        self.density: int = density
        self.layers: int = layers

        self.resources: list = []
        self.alloys: list = []
        self.components: list = []

        # Resource import from JSON
        with open('config/resources.json', 'r') as f:
            data = json.load(f)

        for i in data["resources"]:
            resource = Resource(i["name"], i["mass"])
            self.resources.append(resource)

        for j in data["alloys"]:
            alloy = Alloy(j["name"], j["cost"], j["tier"], j["mass"])
            self.alloys.append(alloy)

        for k in data["components"]:
            component = Component(k["tier"], k["mass"])
            self.components.append(component)

        self.commodities = self.resources + self.alloys + self.components

        # Runs setup function
        self.setup()


    def setup(self) -> None:
        # Function to generate the world

        start_node = System(self.id_count, 0)
        self.systems.append(start_node)

        self.systemGen(start_node,1)

        self.tierAssign()
        self.resourceAssign(list(self.resources))
        self.buildingAssign()
        self.marketAssign()

        pass


    def systemGen(self, source, layer) -> None:
        # Recursive function to create systems according to layers and density

        if layer > self.layers:
            # Breaks out if layer limit has been reached
            return

        for i in range(self.density):
            # A new system is created and added to the node list
            self.id_count += 1
            node = System(self.id_count, layer)

            # Relevant adjacencies are are added
            distance = randint(2,12)
            node.adjacency.append({"system" : source,
                                   "distance" : distance})

            source.adjacency.append({"system" : node,
                                     "distance" : distance})

            # Adds the new node to the list and recurs
            self.systems.append(node)
            self.systemGen(node,layer+1)


    def tierAssign(self):
        # Determine transition points
        interval = self.layers//3
        layer = 0

        for i in range(1,3):
            layer += interval
            self.transition_points[str(i)] = layer

        for sys in self.systems:
            # Uses separate function if a transition pointAdded resources to the Graph class

            if sys.layer in self.transition_points.values():
                # Passes the correct tuple based on transition point
                if self.transition_points["1"] == sys.layer:
                    tiers = (2,3)
                else:
                    tiers = (1,2)

                sys.assignRandom(tiers)

            # Assigns tier based on layer
            elif self.transition_points["1"] > sys.layer:
                sys.assign(3)

            elif self.transition_points["2"] < sys.layer:
                sys.assign(1)

            else:
                sys.assign(2)


    def resourceAssign(self, resources):
        # Assigns basic resources to Tier 1 systems
        all_assigned = False

        for sys in self.systems:
            if sys.tier == 1:
                if all_assigned:
                    # Assigns any random resource
                    resource = choice(self.resources)
                    sys.resources.append(resource)

                else:
                    # Assigns any resource that does not yet exist
                    resource = choice(resources)
                    sys.resources.append(resource)
                    resources.remove(resource)

                # Creates a location where that resource can be gathered
                sys.buildings.append(ResourceGen(resource))

                if not resources:
                    # Changed flag if all assigned
                    all_assigned = True

        if not all_assigned:
            # Repeats if not all resources have been assigned
            self.resourceAssign(resources)


    def buildingAssign(self):
        advanced = False

        for sys in self.systems:
            if sys.tier == 3:
                sys.buildings.append(ManufacturingPlant())

            elif sys.tier == 2:
                num = randint(1,5)
                if 0 < num < 2 or not advanced:
                    sys.buildings.append(AdvancedRefinery())
                    advanced = True

                else:
                    sys.buildings.append(BasicRefinery())

            sys.buildings.append(Station())


    def marketAssign(self):
        # Assigns a market to each system based on tier

        # Resources will be assigned from pools to each market type

        for sys in self.systems:
            if sys.tier == 1:
                sys.market = MiningMarket(sys.resources, self.commodities)

                for i in sys.resources:
                    # Basic resources are added
                    product = MarketItem(i, i.name, randint(1,10),0)
                    sys.market.products.append(product)


            elif sys.tier == 2:
                sys.market = ManufacturingMarket(2, self.commodities)

                # Random alloys, resources and components are filled into the market
                alloy_nums = sample(range(0, len(self.alloys)),2)
                resource_nums = sample(range(0, len(self.resources)), 3)

                for i in alloy_nums:
                    q = randint(1,10)
                    alloy = MarketItem(self.alloys[i], self.alloys[i].name, q, 0)
                    sys.market.products.append(alloy)

                for j in resource_nums:
                    q = randint(1,10)
                    resource = MarketItem(self.resources[j], self.resources[j].name, q, 0)
                    sys.market.products.append(resource)

                q = randint(1,5)
                tier = self.components[randint(0,len(self.components) - 1)]
                component = MarketItem(tier, tier.name, q, 0)
                sys.market.products.append(component)


            elif sys.tier == 3:
                sys.market = ManufacturingMarket(3, self.commodities)

                for i in self.components:
                    q = randint(2, 10)

                    item = MarketItem(i, i.name, q, 0)
                    sys.market.products.append(item)

                alloy_nums = sample(range(0, len(self.alloys)), 2)

                for i in alloy_nums:
                    q = randint(1, 5)
                    alloy = MarketItem(self.alloys[i], self.alloys[i].name, q, 0)
                    sys.market.products.append(alloy)

            sys.market.update()





