import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...sockets.utils import point_list_to_string, string_to_point_list

class CrowdManager_PointViewerNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointViewerNode'
    bl_label = 'Point Viewer'

    node_type = "point"

    point_color : bpy.props.FloatVectorProperty(name="Color", subtype="COLOR", default=(.75, .75, .75), update = CrowdManagerBaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        
    def draw_buttons(self, context, layout):
        layout.prop(self, "point_color")
    
    def edit(self):
        node = self.get_linked_node(0)
        if node is not None:
            pnts = string_to_point_list(node.outputs[0].points)