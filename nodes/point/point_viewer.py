from bgl import GL_POINT
import bpy
from bpy.props import *
from ..base_node import CM_BaseNode
from ...sockets.point_socket import CM_PointProperty

class CM_PointViewerNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_PointViewerNode'
    bl_label = 'Point Viewer'
    bl_width_default = 150

    node_type = ["point", "viewer"]

    GL_COLOR : FloatVectorProperty(subtype="COLOR", size=4, default=(0.75, 0.75, 0.75, 1), min=0, soft_min=0, max=1, soft_max=1, update=CM_BaseNode.property_changed)
    
    GL_POINTS : bpy.props.CollectionProperty(name="Points", type=CM_PointProperty)

    def init(self, context):
        super().__init__()
        self.inputs.new("CM_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        node = self.get_input_node(idx=0)
        if node is not None:
            points = node.outputs[0].points
            col = col.split(factor=min(0.05 + 0.05*len(points), 0.3))
            col.label(text=str(len(points)))
        col.prop(self, "GL_COLOR", text="")

    def edit(self):
        node = self.get_input_node(idx=0)
        self.GL_POINTS.clear()
        if node is not None:
            for p in node.outputs[0].points:
                x = self.GL_POINTS.add()
                x.location = p.location