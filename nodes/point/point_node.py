import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types import CrowdManager_Point as CM_Point
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
        l = [self.point_location.x, self.point_location.y, self.point_location.z]
        r = [self.point_rotation.x, self.point_rotation.y, self.point_rotation.z]
        pnt = CM_Point(l, r)

        points = {"points" : []}

        points["points"].append(pnt.toJSON())

        if len(self.outputs) > 0:
            self.outputs[0].points = json.dumps(points)
        self.link_update()