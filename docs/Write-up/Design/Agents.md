## Archetypes
Each agent will be given an archetype that determines its task. The agent will break down that task into smaller sub-tasks, adding them to a stack in turn - with this process being repeated until each task can be completed within a single cycle. What a agent will do to complete a task will also depend on its archetype.  Each cycle it performs an action such as:
- Buying and selling commodities to the local market
- Check data about other systems
- Travelling between points of interest
- Travelling between systems 
- Producing/consuming a commodity

### How it works
This is the flowchart the agent follows in order to break down the tasks:
![[node action flowchart.png]]


### Example
A given agent's task is to acquire a capacitor. Here's how two different agents would break down this task:
Miner - Leave station -> Move to asteroid belt -> Gather copper ore -> Gather iron ore -> Return to station -> Craft iron ingot -> Craft copper ingot -> Craft capacitor
Entrepreneur - Buy fuel -> Search market boards for  Leave station -> Travel to nearby system -> Enter station
### Archetype trees (need to be added)
## Classes
### General requirements
These are the roles each class must fulfil:
#### Hold an agent's data
This is done with a set of variables attached to the parent agent that hold key information. Some special data points, such as API keys, are declared in the relevant child class to ensure that only needed data is declared and stored. In order to allow an agent to easily change between different ships that may have different stats, data points such as cargo are stored in a separate "ship" class that is taken as a parameter by the agent class.
#### Keep data protected
In order to keep data secure and separated, I used encapsulation for the data points in both the agent and ship classes. This was achieved by making variables private and including get and set methods for each variable, in some cases simplifying by combining set methods where they will be called together. Using these practices means that I can monitor changes and add limits, such as not allowing fuel to go above a ship's capacity. 
### Main agent class
This is the class to store most of an agent's core data points. Each agent is given a name that will act as a unique identifier, allowing us to store and pull the agent's attributes from a database. At the start of it's turn it is sent a copy of the current simulation state and then edits relevant attributes as needed before returning the updated sim state to the main manager.

![[agent class.png|300]]
### Agent child classes
Extra child classes are used to provide unique features for the two core agent types: NPC and Player.

![[npc + player child class.png]]

The NPC class is operated by a local script and therefore has different protocols for accessing its data, as well as necessitating an additional "archetype" attribute. The Player class will be accessed through an external connection, and so has extra functionality to test the connection as well as attributes to store the user's connection type and API key. 
### Ship class
![[ship class.png|400]]

The ship class is treated as a separate object that is then instanced inside the agent. This allows for the ship to easily be stored or traded between agents, and means that cargo and fuel are not tied directly to an agent.

I decided to approach the travel system using the ship class rather than the agent class as it contains the majority of variables that need to be checked and changed when travelling. A simple algorithm is then used that prevents travel if requirements are not met, which looks like this:

![[travel.png]]






