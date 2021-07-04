import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_ObjectPointScatterNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_ObjectPointScatterNode'
    bl_label = 'Object Point Scatter'

    node_type = "point"

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        pass
    
    def update(self):
        pass