
## Problem identification

There is a very large market for advanced simulations attempting to replicate particular industries or situations, such as Microsoft Flight Simulator or Cities: Skylines. They allow for heavy customisation of their respective sims to help with everything from planning to training and therefore afford a very large customer base, however there are very few tools currently on the market that provide a solid foundation to model and build off of a space-based economy.

While there are games such as EVE Online that attempt to create these environments they often take control away from the player, with the main systems built around the idea there will be hundreds of thousands of players participating in the sim. This means that there are very few customisation options to create challenging unique scenarios or test economic theories.

This is where my project comes in, basing the core of the sim on NPCs (non-player characters) who each follow particular archetypes and allow for a greater level of granularity, such as reducing the skill level in some systems or creating a surplus of some resources. In addition to this I plan to make my product open-source meaning that the simulation aspects would be able to be adapted or integrated into other projects. This means that a variety of gameplay styles could be fostered, such as an adventure game like ELITE or an RTS like StarCraft.
## Computational methods

### Why a computational solution is necessary

There are a number of factors that necessitate a computational approach to the problem. The way I plan to approach the simulation involves the individual actions of hundreds of nodes, a scale that would be nearly impossible to achieve without the use of a computer. Additionally these nodes need to be heavily customisable for different situations, which benefits from a computational approach as the effect of changes to the system would be easily and quickly recognisable.

The computer would mainly be used in two circumstances. There is a server side, which is responsible for monitoring and controlling the nodes as well as the API and forms the backbone of the system and takes on most of the processing grunt. There is also the client side, which connects and shares data with the main server and can be customised to provide different overviews and pull different data from the sim.

### Computational methods I will be using

Decomposition will be used to break the project down into smaller steps that need to take place while the simulation is running. This means that the components that I make will be modular and easily swapped out, allowing for easy iteration and development of my product. The steps for the sim running might look like this:

1. Establish connection between server and client, assigning relevant tools & permissions

2. Take any inputs from the client and take action if needed

3. Look at each node and perform an action based on the node’s archetype and status

4. Evaluate any economic or physical impacts on the sim

5. Return any changes or impacts to the client

Abstraction will be used when designing the server infrastructure, as the individual files and data pieces do not need to be known. This will allow me to easily test the functions of the client-server relationships separate from the main sim, meaning that testing will be quick and efficient, and will leave the project open to adaptation to lots of different use cases aside from the sim. It also means that the system will easily be able to be scaled up to larger systems with the addition of compute nodes and clients.

A divide and conquer system will be used when designing the simulation itself by breaking down the systems needed for a single NPC node, then creating a set of archetypes that give each node a set of parameters. This makes it much easier to design the node systems, as I will only be concentrating on one and the effects it has on the environment. It also makes it much easier to scale up and create new nodes as the processes will already be in place.

There will be a large number of both NPC and client nodes that need to exist in the world simultaneously, meaning that I will need to think concurrently in order to balance the actions of each node. If there is a client that is running slightly behind the rest of the sim, it could cause a detrimental impact to some systems. One strategy for doing this is by using a Docker system on the main server, meaning that a number of scripts can be executed at once and are automatically balanced across CPU cores as required.

## Stakeholder

The stakeholder for my project is going to be fans of games such as No Man’s Sky or Elite Dangerous who want to explore deep economy-based mechanics. I will mainly be focusing on those who are more experienced using a computer, specifically navigating mostly text-based interfaces.

They may use the project in order to develop skills regarding problem-solving, breaking down a complex set of requirements into smaller tasks. For instance they may be carrying cargo between two systems, in which case they would look at fuel consumption along a specific route, how they might get more fuel if necessary, what hostile threats they might encounter and how much firepower they can put back out.

They also enjoy strategy-based games such as Civilisation or Catan, as well as some more planning and production games such as Satisfactory or Factorio. This style of gameplay is found in the production and supply chain side of my project, with goods needing safe transport across systems with established routes as well as strategically placed mining outposts and manufacturing facilities.

They hold an interest in economics, looking at how many different effects and events can affect the supply and demand across economies. This will be realistically emulated in the simulation, with it being possible to see impacts on both a micro and macro level across the simulation.

For these reasons the main stakeholder I will be targeting will be Archie, a 17-year-old who is in my Computer Science class, as well as Benjy who is also 17 and is a friend from school. They both hold a strong interest in a lot of similar games and will be a good indicator of what features my stakeholders are looking for. They are also easily contactable and is available for interview and feedback throughout the development of the project.

## Interview

### Questions

⇒ What space-based games have you played before?

╠ What activities or mechanics did you enjoy the most?

╚ What did you feel didn’t work well/was missing?

This is to get a sense of what features in space games are most liked so I can include them, and avoid any mistakes/disliked elements that the stakeholder might dislike.

⇒ What economy-based games have you played before?

╠ What activities or mechanics did you enjoy the most?

╚ What did you feel didn’t work well/was missing?

The economic model for my project could vary between a focus on realism or simplicity, so it is very important to see what my stakeholders prefer when balancing the different systems.

⇒ Do you prefer graphical or text-based interfaces?

This will help to guide me when creating the client, and whether it is necessary to create a more visual interface rather than focusing on text. It may also be possible to allow the user to create their own interface and lay it out how they desire.

⇒ Do you prefer games that are simpler or more complex in their mechanics? Why?

This will help me when balancing the difficulty of the mechanics in my project. If the components are too complex, it may turn people away and reduce my potential userbase. If they are too simple, there may be a lack of depth for players to engage with, resulting in a lack of retention.

⇒ Do you enjoy modding and customising games? Why/why not?
One of the core concepts for the project is a focus on openness and customizability. It will be interesting to see some of the benefits/drawbacks my stakeholders see as a part of this so that I can balance the level of this in the end product.

### Response #1 - Archie

⇒ What space-based games have you played before? EVE online

╠ What activities or mechanics did you enjoy the most? Large scale economy

╚ What did you feel didn’t work well/was missing? Too long of travel times

⇒ What economy-based games have you played before? EVE, Hypixel Skyblock

╠ What activities or mechanics did you enjoy the most? large scale trading and transfer of skills through a median currency

╚ What did you feel didn’t work well/was missing? Can be complicated to start

⇒ Do you prefer graphical or text-based interfaces? Graphical

⇒ Do you prefer games that are simpler or more complex in their mechanics? Why? More complex as it rewards strategical gameplay

⇒ Do you enjoy modding and customising games? Why/why not? Yes as it can add onto the original content of the game in a positive way

### Response #2 - Benjy

⇒ What space-based games have you played before? Kerbal Space Program, No Man’s Sky, unnamed space idle, Star Wars Squadrons, Factorio, Reassembly

╠ What activities or mechanics did you enjoy the most? Ship building, Factions, Character variety (such as aliens)

╚ What did you feel didn’t work well/was missing? Too many microtransactions

⇒ What macro-economy-based games have you played before? Civ 6, Hypixel Skyblock, Minecolonies, Space Warlord Organ Trading Simulator

╠ What activities or mechanics did you enjoy the most? customizable strategies, player driven economy

╚ What did you feel didn’t work well/was missing? too many currencies, illegible numbers

⇒ Do you prefer graphical or text-based interfaces? Graphical with a little bit of graphs

⇒ Do you prefer games that are simpler or more complex in their mechanics? Why? More complex, allows skill expression/organisation > grinding or luck

⇒ Do you enjoy modding and customising games? Why/why not? No, mods generally ruin the narrative/core gameplay of games, except when made by devs that consider the intention behind games
### Analysis

Both of my stakeholders have experience with a variety of space and economic games. One of the main complaints was the complicated nature of currencies and systems in games such as EVE and Hypixel Skyblock, as well as the microtransactions found in these games. They also both enjoyed deeper mechanics so long as they were introduced slowly and didn’t overwhelm the player, as they provide a more enjoyable experience overall.

Archie was strongly in favour of modding, however Benjy prefers mods that respect the original intention behind games. This could be implemented using an official mod loader that recommends approved mods. They also both preferred a graphical interface, with graphs to show some statistics, so I need to find a way of implementing this.
<a id="competitors"></a>
## Competitors

### Eve Online

One of the main inspirations was Eve Online as it provides a very realistic economy simulation. The vast majority of components and resources found across the world of New Eden are either harvested or manufactured by other players, allowing for volatile prices of commodities.

A tier system is used to differentiate components and their general capability, with manufacturing processes used to develop products from T1 -> T2 -> T3 and so on. Time cost becomes a factor due to the fact that most higher-level components can only be found far from the inhabited systems, meaning that roles are created purely from funnelling materials from “nullsec” areas (with little to no security presence) to “highsec” areas where most manufacturing is located.

![[security.png]]

 This leads to analysis of concepts such as time and opportunity cost that can create loopholes in markets and provide fun experiences for players taking advantage of them, with all of the activities in the game feeding back into the main core systems. This is something I think works very well and will make a fun and engaging core for my project.

The graphics are fairly limited, however this means that the core systems and gameplay are the focus, with the UI providing a variety of built-in menus and tools that allow you to monitor different systems and features. The theming and options all fit within the context of the game and work well together, and I will be taking heavy inspiration from it to make a similarly clear but practical interface in my project.

![[eve ui.png]]

Many of the main features of EVE are locked behind a subscription, as well as the premium currency of Plex being both purchasable with real money and sellable on the in-game markets. This leads to pay-to-win elements with certain aspects of the game designed to be tedious/difficult to encourage spending, with the game often being referred to as a “spreadsheet simulator”. The main focus for a game such as this should be its incredibly detailed and realistic economy and EVE fails at this on multiple levels, so I will be careful not to implement similar systems in my project to make the game more accessible and more fun.

### Elite Dangerous

 One of the main components of Elite Dangerous is ship outfitting, with different modules using up one of a limited number of slots. This allows for specialisations in both the hull of the ship (including number of hardpoints and base stats), as well as the loadout of tools and weapons. One benefit from this is that there are larger “freighter” ships in the game that can carry smaller ships, meaning that large sigma amounts of cargo can be shipped across systems while carrying frigates or even other small ships for combat if necessary. I very much enjoy the process of ship hunting and outfitting, with parts often being scattered across multiple systems, following potentially dangerous routes, and is something I plan to implement in my project.
 
 ![[elited ship.png]]

The fuel system in the game adds more strategy when moving between different systems, with some routes taking longer but stopping in more populated systems and some going through less populated areas and necessitating fuel scoops. I plan to use a similar system to this in my project, as if it was implemented into a more detailed economic setting, it could further develop freight and transport roles and add more factors to the supply and demand of goods.

Elite Dangerous focuses significantly more on an NPC-driven economy, with systems being given classifications based on their specialisations and resources available. This results in a list of imports and exports that become relevant to the player when trading and taking missions, with tasks often involving “boom time deliveries” with a strict time limit or sabotage that can affect your standing with local law enforcement. These sometimes add more strategy in regard to a route you might take to get to a destination, with a detour to a further station potentially netting you a big payout, which is why I want to add a similar system.

![[elited station.png]]

 The game often simplifies or allows circumvention of certain mechanics in favour of ease-of-use and moment to moment gameplay. This results in some very interesting ideas that could provide additional layers of strategy not having a large impact on gameplay, so I plan to make these mechanics the focus of my project, sacrificing some of the visual quality that Elite Dangerous provides.

One of the main flaws in Elite Dangerous is that the balancing between different jobs is often very poor, with certain activities such as mining earning significantly more than others. This results in a gameplay experience that can quickly become quite stale, with systems and stations often looking identical. Especially in the later stages of the game ship builds can also boil down to pre-established metas, so in my project I plan to add more variety in both the missions you undertake and the ship parts that are available.

### No Man’s Sky

Space station cores can be “hacked” to create an outlaw station, with specialty vendors that offer illegal goods. This results in upgrades such as signal jammers, which prevent the scanning of your ship’s cargo, and advanced weaponry to become essential when transporting these items to rich economies that can be a number of jumps away. Feeding into this is the necessity for “Warp Cells”, which act as fuel for your starship to jump between systems and must be crafted from materials found on different planets – all resulting in an exciting high risk, high reward system that I think would fit well my project.

One of the core features of No Man’s Sky is the addition of Freighters. These are extremely large starships that can act as portable storage for starships, resources and land vehicles. They are generally very expensive, however they give the player a significant number of options when it comes to completing different tasks – such as a trader installing an economy scanner and a galactic trade terminal or a pirate with a selection of fighters. I think the usefulness of this is slightly undermined, however, as ships can be summoned from anywhere and players can easily use teleport termini to fast-travel between visited systems. In my project I plan to use a similar system as a very late-game purchase as the player’s starships and resources will have fixed locations otherwise.

![[nms freighter.png]]

No Man’s Sky places heavy emphasis on the base stats and looks of a ship, with ships being purchased from NPCs that can be found in stations and major outposts. Each ship falls into a class (ranging from C to S) that determines most of its base stats, in addition to a type (such as hauler or fighter) that may provide extra features catered to a particular playstyle, as well as a visual identity. Ships can also be synthesized, using parts such as wings or hulls found by scrapping other ships and a core of a specific class.

 There are a number of star systems of particular colours that require advanced hyperdrive upgrades to reach. These systems provide unique resources that are very scarce in other economies, and are required in late-game crafting, meaning that they hold a very high value in those places. Additionally the economies found in these systems are unique as items that are very common elsewhere – particularly manufactured goods – hold high demand and low supply. This allows for trade routes through these systems to sell goods high where they would otherwise be low and vice versa. I very much like these mechanics and I think it adds more depth to trader gameplay, with the possible addition that pirate activity is more common and therefore that these locations are more dangerous unless properly outfitted.

![[nms galaxy.png]]

### Lemonade Stand

The main gameplay loop of lemonade stand revolves around making economic choices based on market conditions. Customer flow can be predicted with factors such as weather and temperature, and resources can be purchased at the start of each day that are used up based on customer demand. One thing I enjoy about this is that the system is very easy to understand yet offers a lot of mechanical depth, and the user is encouraged to learn patterns across different days that then help them make more informed choices in the future. In my project I will to aim for a similar outcome with a system that can be learnt from and predicted.

Another element is the price and quality of the product sold. This allows the user to experiment with different values that produce different results, leading them to become more acquainted with the systems in the game such as customer demand. I like this as it allows the user to try and apply what they've learnt about economic principles and the game itself to try and earn the most money, and so is something I will look to implement. 

![[leamonade stand.png|500]]

One issue with the game is that outside of the main supply and demand mechanics, there are not many other features - meaning that user retention is very low as the system can easily be understood and exploited in a fairly short amount of time. This is something I want to try and avoid by introducing a range of economic systems to keep users engaged and provide more unique scenarios to challange their knowlodge and ability. 


### Overall likes & dislikes

One of the main things that I enjoyed – and something that held some other competitors back – was the manufacturing and economy systems found in EVE Online. I plan to integrate this with some of the faction + pirate mechanics from No Man’s Sky to include illegal goods and smuggling routes, introducing security ratings and adding more planning to trade routes.

I would like to use the ship outfitting systems from Elite Dangerous as they provide a good balance of allowing the user to customise and balance their ship while still maintaining the mechanical depth that comes from sourcing the necessary components. I plan to combine this with some of the ship archetypes found in No Man’s Sky to provide a simpler option to beginning players or those just starting a new profession. These will come with a pre-determined set of upgrades and stats while still offering the opportunity to customise and experiment.

One thing I will be avoiding is the microtransaction systems found in Elite Dangerous and EVE Online as they severely limit the level of customisation and personalisation available to most players. Additionally they offer pay-to-progress elements that are designed to circumvent or avoid some elements of the game, giving motivation to make aspects less enjoyable in order to encourage spending – something I dislike and will be avoiding.

I dislike the new player experience in EVE and Elite Dangerous as they offer limited support to the player in regard to starting in new industries due to the pre-established player base and meta. For this reason I plan to keep a few systems sectioned off for new players, featuring the main systems at a more basic and contained level, as well as providing the resources to help them learn the systems and experiment themselves.


<a id="features-of-solution"></a>
## Features of the proposed solution

### Initial concept

My solution will work off the idea of a central manager that will act as a bridge between the two main components of the program; the "nodes" (that make decisions and perform actions) and the economic simulation. 

Each node can either be controlled by a player or the computer. When under the computer, known as an NPC node, it will look at its current circumstances as well as the current state of the simulation and create heuristic values for each possible action. These are influenced by the base "archetype" of the node, including data such as profession or training, to provide reasonable responses to a given situation or choice. It will use these values along with weightings that determine the cost of an action in order to make decisions as to its next move. 

Player controlled nodes receive and send data in the same way that an NPC node does - however they are controlled by a user, whether locally or connecting through the server. They will be provided with an interface that will allow them to see the current sim state and push new actions, with decisions being made either by the user or an external program. 

Actions themselves are tasks performed by the node that have three main data points: cost, speed, and outcome. The cost is everything that is needed for the action to be performed, whether that is a resource cost (such as fuel or money), a social cost (a certain standing with a faction or other group) or a physical requirement such as ship-mounted scanner. Speed determines how many game "cycles" before the node is free to perform another action. The outcome is any positive or negative effects on the node and environment - such as receiving a particular resource or increasing the price of a commodity. Both the speed and outcome might be affected by the cost that the node fulfilled. 

The economic simulation will be updated once each cycle and changes data points based on the outcomes from that cycle. It uses the outcomes from that cycle to calculate new commodity prices, which then are reflected in the game state. It is responsible for the interactions between nodes and groups, as well as the choices that they make, and therefore makes up the core of the simulation as a whole.
### Limitations

Given the real time nature of the sim, some choices or activities may take a longer time to complete when operating in a shared environment. Additionally, as the mechanics are so complex, the user interface will be mainly text-based and simple. This may reduce the potential audience for the game as it will rely on a basic knowledge of command-line tools.

As there are a large number of NPCs running simultaneously, a server with a high number of CPU cores will be necessary. I will be using a Raspberry Pi cluster for development and testing, however for larger instances the user will need to have access to bigger servers. Due to the reliance on the server a basic knowledge of port forwarding and network tools will be needed, with both admin access to the local network and the use of a UNIX-based system.

## Hardware requirements

A main server to run the simulation, with a larger number of CPU cores to handle each of the NPC nodes concurrently. For testing I will be using a Raspberry Pi cluster running through a Power over Ethernet (PoE) switch.

A storage device such as an SSD to store the state of both the simulation and the nodes (both player and computer controlled).

A management device to connect into the server using SSH to adjust processes and monitor performance, using a Unix-based system such as MacOS or Linux.

Client devices for each of the player-controlled nodes with internet access to connect to the main server, running a desktop operating system.

### Software requirements

Docker running on the main server, under either a swarm or desktop configuration – this allows me to manage each of the scripts and components easily and have them running dynamically and concurrently.

Pre-compiled C++ binaries – this allows for the scripts to run on different systems without the need for an interpreter.

GitHub – this allows me to easily back up and share project files, as well as monitor version releases and changes.

CLion - this is a C family IDE that allows for Git integration as well as remote development, meaning that I can access and back up my code and scripts easily.

Rccp – a C++ library that allows me to use the R programming language for calculations and economy simulation.

Desktop environment for each client – so they are able to access the simulation and control their nodes.

## Success Criteria


| Criteria                                                                                               | How to evidence                                                                                                             |
| ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| The player can log on                                                                                  | An account that can be used to access the controls                                                                          |
| There is an authentication system to restrict what a user can access                                   | An account for a base user is unable to access admin settings                                                               |
| There is an interface to control the sim                                                               | An admin is able to log on and adjust various settings and parameters                                                       |
| There are options to edit the NPC nodes                                                                | The behaviour of each node can be modified from the admin panel                                                             |
| There is a networking solution to access the sim from outside the local network                        | Users from outside the network can log in and make changes                                                                  |
| The system can be interfaced with using an API                                                         | An external program is able to pull data from the server, such as number of nodes active                                    |
| There are rate limits on the API so it cannot be abused                                                | One API key is spammed with requests and access is cut off/restricted                                                       |
| The server is able to manage its tasks concurrently and efficiently                                    | Users can log on and adjust the sim while it is running                                                                     |
| There are NPC “nodes” that are able to act autonomously and make decisions                             | Over a longer period of time there are changes to the state of the sim                                                      |
| Nodes may also be controlled by the player directly or through the admin panel                         | Once a setting is adjusted there is a change in the node’s behaviour                                                        |
| There are a number of systems that unique attributes and can be travelled between                      | A player is able to assess conditions across systems and move resources between them                                        |
| Each system, its attributes, the density of systems and size of playable area are randomly generated   | Each version of the sim has a different setup based on a randomly generated seed and the parameters set                     |
| Commodity prices are affected by supply and demand                                                     | When a large quantity of goods are purchased the price increases and vice versa                                             |
| There are interactions between systems based on the behaviour of each node                             | The transportation of goods between two systems affects the economy of both                                                 |
| Each system has a central hub with info about the system                                               | A node can reach a point where they can see local conditions                                                                |
| Each node has a ship that allows them to move between areas                                            | The nodes are able to go from one location to another                                                                       |
| Each ship has certain base stats and options to upgrade them                                           | When a ship has an upgrade module installed it increases the power of/reduces the time to perform an action                 |
| There are various activities for players to do                                                         | There are different ways to make money that influence each other                                                            |
| There are chains of manufacturing based across different systems                                       | There is a clear path of raw materials, through manufacturing facilities and to an end product.                             |
| A closed system is created, meaning that there are no external sources of products, ships or materials | All resources purchased and sold can track back to base materials harvested by a node                                       |
| The system is modifiable by the user and allows for plugins to customize what features are available   | The user is able to create and install a plugin that results in a change in behaviour of the sim                            |
| There are clear instructions to allow a user to create their own instance of the sim                   | Users who may have less programming experience are able to understand how it works and can set it up                        |
| The source code is available for people to edit and adjust to their needs                              | There is a public and easy to access source containing the full code of the sim under a FOSS (free and open source) licence |
