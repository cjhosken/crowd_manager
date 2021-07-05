import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.point import CM_PointList, CM_Point
class CrowdManager_PointNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointNode'
    bl_label = 'Point'
    bl_width_default = 350

    node_type = "point"

    point_location : bpy.props.FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0), update = CrowdManagerBaseNode.property_changed)
    point_rotation : bpy.props.FloatVectorProperty(name="Rotation", subtype="EULER", default=(0, 0, 0), update = CrowdManagerBaseNode.property_changed)
    points : bpy.props.StringProperty(name="Points", default=CM_PointList().toJSON())

    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        layout.prop(self, "point_location")
        layout.prop(self, "point_rotation")
    
    def edit(self):
        points = CM_PointList(dict=CM_PointList.fromJSON(self.points))

        loc = [self.point_location.x, self.point_location.y, self.point_location.z]
        rot = [self.point_rotation.x, self.point_rotation.y, self.point_rotation.z]

        if len(points.points) == 0:
            pnt = CM_Point(loc=loc, rot=rot)
            points.add(pnt)
            self.link_update()

        else:
            if points.points[0].location != loc or points.points[0].rotation != rot:
                points.points[0].set(loc=loc, rot=rot)
                self.link_update()

        self.points = points.toJSON()
        self.outputs[0].points = self.points

