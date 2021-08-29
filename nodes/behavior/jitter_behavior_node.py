import bpy
from bpy.props import BoolVectorProperty, FloatProperty, BoolProperty
from ..base_node import CrowdManager_BaseNode


class CrowdManager_JitterBehaviorNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_JitterBehaviorNode'
    bl_label = 'Jitter Behavior'
    bl_width_default = 200

    limit_axis: BoolVectorProperty(name="Limit Axis", description="axis jittering is constrained to", subtype="XYZ", default=(
        True, True, True), update=CrowdManager_BaseNode.property_changed)

    use_location: BoolProperty(name="Position", description="enable positional jittering", default=True)
    use_rotation: BoolProperty(name="Rotation", description="enable rotational jittering", default=True)

    strength: FloatProperty(name="Strength:", description="jittering strength",
                            min=0, default=1, update=CrowdManager_BaseNode.property_changed)

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        col = layout.column()
        row = col.row()
        row.prop(self, 'use_location', toggle=1)
        row.prop(self, 'use_rotation', toggle=1)
        row = col.row()
        row.prop(self, 'strength')
        row = col.row()
        row.prop(self, "limit_axis", text="", toggle=1)

    def edit(self):
        code = f"""
import bpy
import random


PX = LAST_SIM.location.x
PY = LAST_SIM.location.y
PZ = LAST_SIM.location.z

if {self.use_location}:    
    if {self.limit_axis[0]}:
        PX += random.uniform({-self.strength}, {self.strength})

    if {self.limit_axis[1]}:
        PY += random.uniform({-self.strength}, {self.strength})

    if {self.limit_axis[2]}:
        PZ += random.uniform({-self.strength}, {self.strength})

RX = LAST_SIM.rotation.x
RY = LAST_SIM.rotation.y
RZ = LAST_SIM.rotation.z

if {self.use_rotation}:
    if {self.limit_axis[0]}:
        RX += random.uniform({-self.strength}, {self.strength})

    if {self.limit_axis[1]}:
        RY += random.uniform({-self.strength}, {self.strength})

    if {self.limit_axis[2]}:
        RZ += random.uniform({-self.strength}, {self.strength})

LOCATION = [PX, PY, PZ]

ROTATION = [RX, RY, RZ]

OUTPUT = [LOCATION, ROTATION]
        """

        self.outputs[0].code = code

        self.linked_update()
