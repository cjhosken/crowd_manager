import bpy
import gpu
from gpu_extras.batch import batch_for_shader
import bgl
import math
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.point import CM_PointList, CM_Point

GL_POINTS = []
class CrowdManager_PointViewerNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointViewerNode'
    bl_label = 'Point Viewer'

    node_type = "point"

    linked : BoolProperty()
    point_color : FloatVectorProperty(subtype="COLOR", size=4, default=(0.75, 0.75, 0.75, 1), min=0, soft_min=0, max=1, soft_max=1, update=CrowdManagerBaseNode.property_changed)

    def init(self, context):
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        
    def draw_buttons(self, context, layout):
        col = layout.column()
        node0 = self.get_linked_node(0)
        if node0 is not None:
            points = CM_PointList(dict=CM_PointList.fromJSON(node0.outputs[0].points))
            col = col.split(factor=min(0.05 + 0.05*len(str(points.points)), 0.3))
            col.label(text=str(len(points.points)))
        col.prop(self, "point_color", text="")

    def edit(self):
        node0 = self.get_linked_node(0)
        if node0 is not None:
            points = CM_PointList(dict=CM_PointList.fromJSON(node0.outputs[0].points))
            pc = self.point_color
            pnt = []
            col = []
            for p in points.points:
                pnt.append((p.location[0], p.location[1], p.location[2]))
                col.append((pc[0], pc[1], pc[2], pc[3]))

            for i, s in enumerate(GL_POINTS):
                if str(s[0]) == self.name:
                    GL_POINTS[i] =  [
                            self.name,
                            pnt,
                            col
                        ]
                    break
            else:
                GL_POINTS.append([
                    self.name,
                    pnt,
                    col
                ])

    def clear_points(self):
        for i, s in enumerate(GL_POINTS):
            if s[0] == self.name:
                GL_POINTS.pop(i)

    def free(self):
        for i, s in enumerate(GL_POINTS):
            if s[0] == self.name:
                GL_POINTS.pop(i)
    
    def update(self):
        for i in self.inputs:
            if i.links:
                if not self.linked:
                    self.edit()
                    self.linked = True
            else:
                if self.linked:
                    self.edit()
                    self.clear_points()
                    self.linked = False