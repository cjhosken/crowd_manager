from bgl import GL_POINT
import bpy
from bpy.props import *
from ..base_node import CrowdManager_BaseNode

class CrowdManager_PointTransformNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_PointTransformNode'
    bl_label = 'Point Transform'

    node_types = ["point"]

    point_translate : bpy.props.FloatVectorProperty(name="Translate", subtype="TRANSLATION", default=(0, 0, 0), update=CrowdManager_BaseNode.property_changed)
    point_rotate : bpy.props.FloatVectorProperty(name="Rotate", subtype="EULER", default=(0, 0, 0), update=CrowdManager_BaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new("CrowdManager_PointSocketType", "Points")
        self.outputs.new("CrowdManager_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "point_translate")
        col.prop(self, "point_rotate")

    def edit(self):
        pnts = self.outputs[0].points
        node = self.get_input_node(idx=0)

        pnts.clear()

        if node is not None:
            for p in node.outputs[0].points:
                x = pnts.add()
                x.location = (p.location.x + self.point_translate.x, p.location.y + self.point_translate.y, p.location.z + self.point_translate.z)
