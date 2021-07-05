import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.point import CM_PointList, CM_Point

class CrowdManager_PointViewerNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointViewerNode'
    bl_label = 'Point Viewer'

    node_type = "point"

    linked : BoolProperty()

    def init(self, context):
        self.inputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        node0 = self.get_linked_node(0)
        if node0 is not None:
            points = CM_PointList(dict=CM_PointList.fromJSON(node0.outputs[0].points))
            layout.label(text=str(len(points.points)))

    
    def edit(self):
        node0 = self.get_linked_node(0)
        if node0 is not None:
            points = CM_PointList(dict=CM_PointList.fromJSON(node0.outputs[0].points))
            for p in points.points:
                print(p)

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

