# Behavior Scripting
The crowd manager addon gives you the ability to program your own behaviors. To use this, simply create the `Script Behavior` node and link a text/python file. *This file can be internal, and doesnt need an extension*

## API
Here's some useful api references that make accessing agent data easier.

### References

`FRAME` : Current Frame

`AGENTS` : All Agents

`AGENT` : Agent Object

`LAST_SIM` : Previous simulated point

``


## Code Structure

An example of a basic position jitter behavior.

```py
import bpy
import random

LOCATION = [
    LAST_SIM.location.x + (random.random() - 0.5) * 2, 
    LAST_SIM.location.y + (random.random() - 0.5) * 2, 
    LAST_SIM.location.z + (random.random() - 0.5) * 2
]
ROTATION = [0, 0, 0]


OUTPUT = [LOCATION, ROTATION]
```
