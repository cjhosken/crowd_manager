# Behavior Scripting
The crowd manager addon gives you the ability to program your own behaviors. To use this, simply create the `Script Behavior` node and link a text/python file. *This file can be internal, and doesnt need an extension*

## API
Here's some useful api references that make accessing agent data easier.

### References

`FRAME` : Current Frame

`AGENTS` : All Agents

`AGENT` : Agent Object

`LAST_SIM` : Previous simulated point

`OUTPUT` : Behavior code output. First index is location, second is rotation. *must be an array of size 2*

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

Every behavior script must end with `OUTPUT = [LOCATION, ROTATION]`. The variable names can be different, but if you do not include the location and rotation vectors in the `OUTPUT` list the addon will crash. Otherwise, everything else can be programmed just like you would in python.
