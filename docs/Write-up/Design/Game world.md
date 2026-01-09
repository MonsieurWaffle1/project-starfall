## Systems(?)
### This needs to be sorted and made better
The game world is made up of a series of procedurally generated "systems", each with a list of points of interest (POIs) that can be visited by a agent. These come in three types: 
- Hub stations that have a market with local prices for each commodity, an inventory of goods for purchase, a refuelling source, basic fabrication capabilities, as well as a small hanger for agents to store their ships and goods
- Harvesting sites that allow for the extraction of commodities with specific tools
- Agent-produced stations that fabricate higher tier commodities from lower tier ones as well as provide a much larger hanger for ships and cargo 

Additionally, each system is given a security rating of either "low sec" or "high sec". This defines three things:
- The safety of the system. In low sec systems there is no consequence for attacking other agents and an agent will drop all of its cargo upon its ship being destroyed, and agent-produced stations can be griefed requiring repairs - however in high sec systems these actions carry fines.
- The rarity of commodities provided. Low sec systems contain rarer commodities that are needed to produce higher tier technologies and components, and need specialised equipment to extract.

Each system is an instance of the "system" class, itself containing a list of POIs that are instances of their respective type, each inheriting from the "POI" class. These are the diagrams for each type:
[Class diagrams for systems/POIs]

### Specialisations
#### Industrial
An industrial specialisation produces and provides commodities for other systems, sells goods for a lower price, and has a comparatively poorer economy - resulting in a lower security level. These specialisations are split into three tiers to match the three commodity tiers:
- Tier 1 systems extract raw resources such as iron or aluminium ore
- Tier 2 systems refine these resources into alloys, composites and bars that can be used in production
- Tier 3 systems combine and mould these resources into advanced components such as microchips and wiring
#### Economic
Economic systems have a comparatively better economy - resulting in them being a hub for most large scale trade and activity. They also contain the most advanced level of manufacturing plants that take tier 2 and 3 commodities and produce packaged components, such as weaponry and starships. 
### Game map
#### Layout
The game map is made up of *n* systems, each connected by a "wormholes" of varying lengths - represented by a weighted graph. The world is generated using a hub-and-spoke model, with systems at the centre of the graph being more wealthy and economic, and systems further from the centre become progressively more industrial and less wealthy. Here's an example of how this looks in practice:

![[really cool graph.png]]
#### Storage
Each system (or "node") is given a unique identifier when it is generated and then its data is stored in a database. In order to map out the edges that connect these nodes, we use an adjacency list stored as a dictionary:
```
adjacencyList = {
	0:[1,2]
	1:[0,3]
	2:[0,3]
	3:[1,2]
}
```
This shows for a given node what edges it has connecting it to other nodes, such as node with ID 0 having edges connecting it to nodes 1 and 2. We can improve this by adding the length of each edge:
```
adjacencyList = {
	0:[[1,4],[2,8]]
	1:[[0,4],[3,2]]
	ect.
```
We can now build up a complete picture of our graph without the space waste that an adjacency matrix introduces over a large number of edges.
## Generation
### Notes to self ignore pls
- Security (boolean)
- Econ strength
- Player built structures (list)



Each system is represented by a node on a weighted graph, with the weights on each graph representing the distances between each system. To begin with a "core" system is generated based off of a seed - an integer that will form the basis of each random event. Each subsequent system is added moving outwards from the core system, with the attributes of a new node generated based off of it's neighbours. 

There are two possible forms of inheritance - pure inheritance and semi inheritance - that are both make use of an inheritance algorithm. 
### Inheritance algorithm 
Our inheritance algorithm should produce probabilities that total to one and favour nodes that are a shorter distance away.

Take an example such as this:
![[generation example 1.png]]
In this case, there are 2 high sec systems and 1 low sec system. First the distance to each node are added:
$$2 + 4 + 5 = 11$$

Currently, these probabilities favour nodes further away. To fix this, we find the reciprocal of each probability:
$$\frac{1}{4},\frac{1}{5},\frac{1}{2}$$
Now we need to make sure that these probabilities add to 1. We find the sum of the reciprocals:
$$\frac{1}{4}+\frac{1}{5}+\frac{1}{2}=\frac{19}{20}$$
We then divide each value by the sum of reciprocals:
$$(\frac{1}{4}*\frac{20}{19})+(\frac{1}{5}*{\frac{20}{19}})+(\frac{1}{2}*\frac{20}{19})$$
This then gives us our set of probabilities: 
$$\frac{5}{19},\frac{4}{19},\frac{10}{19}$$
We then use these in order to generate the attribute. Here is the psudocode for this process:
```
probs = [lengths of edges]
total = 0

for i in probs:
	i  = i^(-1)
	total += i

for i in probs:
	i = i * total

generate number between 1 and (number of edges) using (probs) and (seed)
```
### Pure inherited attributes
A pure inherited attribute 

#### Security


### Semi-inherited attributes
A semi-inherited attribute is designed such that similar attributes appear relatively close to each other on the game map, with a small element of randomness to introduce variety. Influence is taken from adjacent systems, with an algorithm using this to generate a new attribute.

#### Specialisations 
##### Class structure
Any possible specialisation for a system comes under one of two categories: industrial or economic. 

An industrial specialisation produces and provides commodities for other systems, sells goods for a lower price, and has a comparatively poorer economy - resulting in a lower security level. These specialisations are split into three tiers to match the three commodity tiers:
- Tier 1 systems extract raw resources such as iron or aluminium ore
- Tier 2 systems refine these resources into alloys, composites and bars that can be used in production
- Tier 1 systems combine and mould these resources into advanced components such as microchips and wiring 

Economic systems hold a higher level of security, and represent safe hubs for large scale trade and activity. Commodities are funnelled here by traders from industrial systems for advanced manufacturing, producing advanced products and technologies that are then hauled back out into the industrial systems to be used. Examples of potential specialisations include arms, starships or refinery equipment.

A given industrial or economic system may have more then one specialisation, and all specialisations must appear at least once in each generated game world.
##### Generation
When filling out our blank game world with specialisations, we first fill it out with our basic specialisations. We want to make sure we have an even balance of specialisation types, so we assign $\frac{1}{4}$ of the total number of layers to each type. Due to the way the world is initially generated, this naturally results in more T3 industrial than T2 industrial, more T2 than T1 and so on.

First we determine our transition points:
```
types = [e, t1i, t2i, t3i]
currentType = 0

// Determine the transtion points
numOfLayers = len(layers)
transitionPoints = []

for i in range (1,4):
	transitionPoints.append(layers[numOfLayers/i])
```
Next we assign the types to our systems, making sure we have a gentle transition between types by letting them bleed into each other:
```
// Assign types
for i in range (0,layers):
	layer = layers[i]
	
	if layerNumber in transitionPoints:
		transition = true
	else:
		transition = false
	
	for system in layer:
		if transition:
			system.type = types[random(currentType or currentType + 1)]
		else:
			system.type = types[currentType]
			
	
	if transition:
		currentType += 1
```
After this, we add specific resources and specialisations to our systems. Each specialisation must appear in a system at least once, and every system must have at least one specialisation. First we loop through each system, adding a random attribute from the list and keeping track of the number of unique attributes that have been generated:
```
generatedAttributes = []

for system in systems:
	possibleAttributes = possible varations leading from system.type
	attribute = possibleAttributes.random()
	system.attributes.append(attribute)
	
	if attribute not on generatedAttributes:
		generatedAttributes.append(system.attribute)

```
Next, we check to make sure that all possible attributes have actually been generated, by comparing our lists of possible and generated attributes:
```
missing = queue()

for attribute in possibleAttributes:
	if attribute not in generatedAttributes:
		missing.append(attributes)
```
Finally we go back through our system list, assigning any missing attributes:
```
while size(missing) > 0:
	for system in systems:
		attribute = missing.pop()
		system.attributes.append(attribute)
```
#### Economic strength















