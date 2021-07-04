import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...sockets.utils import point_list_to_string, string_to_point_list
class CrowdManager_PointNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointNode'
    bl_label = 'Point'
    bl_width_default = 350

    node_type = "point"

    point_location : bpy.props.FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0), update = CrowdManagerBaseNode.property_changed)
    point_rotation : bpy.props.FloatVectorProperty(name="Rotation", subtype="EULER", default=(0, 0, 0), update = CrowdManagerBaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        layout.prop(self, "point_location")
        layout.prop(self, "point_rotation")
    
    def update(self):
        pnt = [self.point_location, self.point_rotation]

        if len(self.outputs) > 0:
            self.outputs[0].points = point_list_to_string([pnt])
        self.link_update()