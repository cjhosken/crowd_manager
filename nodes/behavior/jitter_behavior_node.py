import bpy
import json
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_JitterBehaviorNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_JitterBehaviorNode'
    bl_label = 'Jitter Behavior'
    bl_width_default = 150

    axis : BoolVectorProperty(default=(True, True, True), update=CM_BaseNode.property_changed)

    strength : FloatProperty(default = 1, update=CM_BaseNode.property_changed)

    node_type = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CM_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, 'strength', text="Strength")
        row = col.row()
        row.prop(self, "axis")
    
    def edit(self):
        code = f"""
import bpy
import random

if {self.axis[0]}:
    X = LAST_SIM.location.x + (random.random() - 0.5) * (2*{self.strength})
else:
    X = LAST_SIM.location.x

if {self.axis[0]}:
    Y = LAST_SIM.location.y + (random.random() - 0.5) * (2*{self.strength})
else:
    Y = LAST_SIM.location.y

if {self.axis[0]}:
    Z = LAST_SIM.location.z + (random.random() - 0.5) * (2*{self.strength})
else:
    Z = LAST_SIM.location.z

LOCATION = [X, Y, Z]

ROTATION = [0, 0, 0]


OUTPUT = [LOCATION, ROTATION]
        """

        self.outputs[0].code = code
        
        self.linked_update()