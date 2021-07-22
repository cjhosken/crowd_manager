import bpy
import json
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_ConstantBehaviorNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_ConstantBehaviorNode'
    bl_label = 'Constant Behavior'
    bl_width_default = 150

    axis : FloatVectorProperty(default=(0, 0, 0), update=CM_BaseNode.property_changed)

    node_type = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CM_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        layout.prop(self, "axis")
    
    def edit(self):
        code = f"""
import bpy
import random

LOCATION = [LAST_SIM.location.x, LAST_SIM.location.y, LAST_SIM.location.z]

if {self.axis[0]}:
    LOCATION[0] = LAST_SIM.location.x + (random.random() - 0.5) * (2*{self.strength})

if {self.axis[1]}:
    LOCATION[1] = LAST_SIM.location.y + (random.random() - 0.5) * (2*{self.strength})

if {self.axis[2]}:
    LOCATION[2] = LAST_SIM.location.z + (random.random() - 0.5) * (2*{self.strength})


ROTATION = [0, 0, 0]


OUTPUT = [LOCATION, ROTATION]
        """

        self.outputs[0].code = code
        
        self.linked_update()