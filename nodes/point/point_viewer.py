import bpy
from bpy.props import FloatVectorProperty, CollectionProperty
from ..base_node import CrowdManager_BaseNode
from ...sockets.point_socket import CrowdManager_PointProperty


class CrowdManager_PointViewerNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_PointViewerNode'
    bl_label = 'Point Viewer'

    node_types = ["point", "viewer"]

    GL_COLOR: FloatVectorProperty(subtype="COLOR", size=4, default=(
        0.75, 0.75, 0.75, 1), min=0, soft_min=0, max=1, soft_max=1, update=CrowdManager_BaseNode.property_changed)
    GL_POINTS: CollectionProperty(
        name="Points", type=CrowdManager_PointProperty)

    def init(self, context):
        super().__init__()
        self.inputs.new("CrowdManager_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        node = self.get_input_node(idx=0)
        if node is not None:
            points = node.outputs[0].points
            if len(points) > 0:
                col = col.split(factor=min(0.1 + 0.05*len(points), 0.3))
            else:
                col = col.split(factor=min(0.15, 0.3))
            col.label(text=str(len(points)))
        col.prop(self, "GL_COLOR", text="")

    def edit(self):
        node = self.get_input_node(idx=0)
        self.GL_POINTS.clear()
        if node is not None:
            for in_point in node.outputs[0].points:
                out_point = self.GL_POINTS.add()
                out_point.location = in_point.location
                out_point.rotation = in_point.rotation
