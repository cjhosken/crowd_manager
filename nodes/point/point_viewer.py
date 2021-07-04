import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
import gpu
import bgl
from gpu_extras.batch import batch_for_shader

class CrowdManager_PointViewer(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointViewer'
    bl_label = 'Point Viewer'

    node_type = "point"

    point_color : bpy.props.FloatVectorProperty(name="Color", subtype="COLOR", default=(.75, .75, .75))

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        
    def draw_buttons(self, context, layout):
        layout.prop(self, "point_color")
    
    def update(self):
        node = self.get_linked_node(0)
        if node is not None:
            print(node.outputs[0].points)
