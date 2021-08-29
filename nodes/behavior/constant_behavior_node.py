import bpy
from bpy.props import BoolProperty, FloatProperty, FloatVectorProperty
from ..base_node import CrowdManager_BaseNode

class CrowdManager_ConstantBehaviorNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_ConstantBehaviorNode'
    bl_label = 'Constant Behavior'
    bl_width_default = 250

    node_types = ["behavior"]

    use_location: BoolProperty(name="Position", description="use constant position", default=True, update=CrowdManager_BaseNode.property_changed)
    use_rotation: BoolProperty(name="Rotation", description="use constant rotation", default=True, update=CrowdManager_BaseNode.property_changed)

    location_change: FloatVectorProperty(name="Location", subtype="TRANSLATION", default = (0, 0, 0), update=CrowdManager_BaseNode.property_changed)
    rotation_change: FloatVectorProperty(name="Rotation", subtype="EULER", default = (0, 0, 0), update=CrowdManager_BaseNode.property_changed)

    speed: FloatProperty(name="Speed", default=1)

    def init(self, context):
        super().__init__()

        self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        col = layout.column()
        row = col.row()
        row.prop(self, 'use_location', toggle=1)
        row.prop(self, 'use_rotation', toggle=1)
        if self.use_location or self.use_rotation:
            col.prop(self, 'speed')

        if self.use_location:
            col.prop(self, 'location_change', text="Translate")

        if self.use_rotation:
            col.prop(self, 'rotation_change', text="Rotate")

    
    def edit(self):
        code = f"""
LOCATION = [
    LAST_SIM.location.x + {self.location_change.x} * {self.speed},
    LAST_SIM.location.y + {self.location_change.y} * {self.speed},
    LAST_SIM.location.z + {self.location_change.z} * {self.speed}
]

ROTATION = [
    LAST_SIM.rotation.x + {self.rotation_change.x} * {self.speed},
    LAST_SIM.rotation.y + {self.rotation_change.y} * {self.speed},
    LAST_SIM.rotation.z + {self.rotation_change.z} * {self.speed}
]


OUTPUT = [LOCATION, ROTATION]    
                """
        self.outputs[0].code = code
        
        self.linked_update()