import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_PointNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointNode'
    bl_label = 'Point'
    bl_width_default = 350

    node_type = "point"

    point_location : bpy.props.FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0))
    point_rotation : bpy.props.FloatVectorProperty(name="Rotation", subtype="EULER", default=(0, 0, 0))

    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        layout.prop(self, "point_location")
        layout.prop(self, "point_rotation")
    
    def update(self):
        self.outputs[0].points = None
        self.link_update()