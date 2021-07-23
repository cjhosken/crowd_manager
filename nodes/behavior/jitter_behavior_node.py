import bpy
from bpy.props import BoolVectorProperty, FloatProperty
from ..base_node import CrowdManager_BaseNode


class CrowdManager_JitterBehaviorNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_JitterBehaviorNode'
    bl_label = 'Jitter Behavior'
    bl_width_default = 200

    limit_axis: BoolVectorProperty(name="Limit Axis", description="axis jittering is constrained to", subtype="XYZ", default=(
        True, True, True), update=CrowdManager_BaseNode.property_changed)

    strength: FloatProperty(name="Strength:", description="jittering strength",
                            min=0, default=1, update=CrowdManager_BaseNode.property_changed)

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, 'strength')
        row = col.row()
        row.prop(self, "limit_axis", text="Limit", toggle=1)

    def edit(self):
        code = f"""
import bpy
import random

if {self.limit_axis[0]}:
    X = LAST_SIM.location.x + random.uniform({-self.strength}, {self.strength})
else:
    X = LAST_SIM.location.x

if {self.limit_axis[1]}:
    Y = LAST_SIM.location.y + random.uniform({-self.strength}, {self.strength})
else:
    Y = LAST_SIM.location.y

if {self.limit_axis[2]}:
    Z = LAST_SIM.location.z + random.uniform({-self.strength}, {self.strength})
else:
    Z = LAST_SIM.location.z

LOCATION = [X, Y, Z]

ROTATION = [LAST_SIM.rotation.x, LAST_SIM.rotation.y, LAST_SIM.rotation.z]

OUTPUT = [LOCATION, ROTATION]
        """

        self.outputs[0].code = code

        self.linked_update()
