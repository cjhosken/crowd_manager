import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.point import CM_PointList, CM_Point

class CrowdManager_PointJoinNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointJoinNode'
    bl_label = 'Join Points'

    node_type = "point"

    linked : BoolProperty()
    points : bpy.props.StringProperty(name="Points", default=CM_PointList().toJSON())

    def init(self, context):
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)

        self.points = CM_PointList().toJSON()
        out_points = CM_PointList(dict=CM_PointList.fromJSON(self.points))


        if node0 is None: 
            if node1 is not None:
                out_points = CM_PointList(dict=CM_PointList.fromJSON(node1.outputs[0].points))
        else:
            if node1 is None:
                out_points = CM_PointList(dict=CM_PointList.fromJSON(node0.outputs[0].points))
            else:
                
                points0 = CM_PointList(dict=CM_PointList.fromJSON(node0.outputs[0].points))
                points1 = CM_PointList(dict=CM_PointList.fromJSON(node1.outputs[0].points))
                for p0 in points0.points:
                    out_points.add(p0)
                for p1 in points1.points:
                    out_points.add(p1)
                
        self.points = out_points.toJSON()
        self.outputs[0].points = self.points
        self.link_update()

    def update(self):
        for i in self.inputs:
            if i.links:
                if not self.linked:
                    self.edit()
                    self.linked = True
            else:
                if self.linked:
                    self.edit()
                    self.linked = False