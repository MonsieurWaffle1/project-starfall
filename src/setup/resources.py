"""
A list of possible resources that can be generated
"""

from ..commodity import *

resources = (
    Resource("aluminium"),
    Resource("titanium"),
    Resource("iron"),
    Resource("copper"),
    Resource("gold"),
    Resource("silver"),
    Resource("platinum"),
    Resource("Palladium"),
    Resource("cobalt"),
    Resource("lead")
)

alloys = (
    Alloy("AlCu",("aluminium","copper"),2),
    Alloy("AgPt",("silver","platinum"),2),
    Alloy("FeAu",("iron","gold"),2),
    Alloy("TiPb",("titanium", "lead"),3),
    Alloy("PdCo",("palladium","cobalt"),3)
)

components = (
    Component(1),
    Component(2),
    Component(3)
)