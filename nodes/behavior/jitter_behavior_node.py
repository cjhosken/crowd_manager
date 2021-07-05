import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode


class CrowdManager_JitterBehaviorNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_JitterBehaviorNode'
    bl_label = 'Jitter Behavior'

    node_type = "behavior"

    jitter_strength : FloatProperty(name="Strength", default=1, update=CrowdManagerBaseNode.property_changed)

    jitter_axis : BoolVectorProperty(name="Axis", subtype="XYZ", default=(True, True, True), update=CrowdManagerBaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_BehaviorSocketType', "Behavior")

    def draw_buttons(self, context, layout):
        layout.prop(self, 'jitter_strength')
        layout.prop(self, 'jitter_axis')
    
    def update(self):
        code = f"import random\nx = (random.random() - 0.5) if {self.jitter_axis[0]}  else 0\ny = (random.random() - 0.5) if {self.jitter_axis[1]} else 0\nz = (random.random() - 0.5) if {self.jitter_axis[2]} else 0\nl = [x*{self.jitter_strength}, y*{self.jitter_strength}, z*{self.jitter_strength}]"
        self.outputs[0].code = code