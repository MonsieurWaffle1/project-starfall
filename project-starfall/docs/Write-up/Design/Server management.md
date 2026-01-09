## General manager

The main manager of the program will need to manage each of the player and non-player agents, linking into the main simulation. It will be ran at launch and act as a bridge between the separate components of the program, and has to: 
- Load up and run each component
- Handle player connections to the server
- Manage each agent's tasks and requests
- Hold a global record of time
- Update and share the game state

Here is an example of how this works:

![[Main manager.png|600]]


**Load up and run each component**
Each of the NPCs are booted and added to a list of connected agents. The current game state is taken from secondary storage and loaded into the program to be distributed to each connected agent. 

**Handle player connections to the server**
One complication with player connections is the potential for abuse, such as through DDOS attacks. To avoid this I decided to use API keys to allow only specific people and devices to connect to the game, with the added benefit of being able to monitor usage and set rate limits. I also took the approach of fetching and executing client requests server-side, meaning that the program is able to send requests to the player rather than player to server reducing the potential for spam requests.

**Manage each agent's tasks and requests**
When designing this system, I wanted to have the functionality for different tasks to take a varying amount of time, with an agent being able to create a list of tasks that are executed in order. To do this I will make use of a number of queue data structures - one with each of the agents currently running, and one for each agent that contains a list of actions. The main manager looks at each agent in turn and checks if it is busy, collecting and starting the next item in the queue if needed.

**Hold a global record of time**
A simple but elegant solution for this can be used. Each time the list of agents has been fully iterated through and the sim is updated, a global "cycle" counter is incremented. This is then printed to each user logged in and is used as the basis for an agents "busy" state.

**Update and share the game state**
In order to prevent agents earlier in the queue from having an advantage, the entire game state is updated at once and once per game cycle. This allows a buffer to prevent micro-trading to influence and take advantage of markets. This new game state can then be accessed by each agent and new actions can be queued based on the outcome.


## Connect a new agent

This function is run each time a user requests to join the sim with a valid API key. The main method of communication will be using "packets" - JSON files sent over the internet that contain key variables and info. Each packet has a header that will contain the player's API key and agent ID to link the attached info to the relevant agent, as well as variables sorted into groups that can then be unpacked and used by the main manager.  

![[connect new nodes.png|400]]
