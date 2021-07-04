import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
import gpu
import bgl
from gpu_extras.batch import batch_for_shader

class CrowdManager_PointJoin(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointJoin'
    bl_label = 'Join Points'

    node_type = "point"

    remove_doubles : BoolProperty(default=False)
    merge_distance : FloatProperty(default = 0.001)

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_PointSocketType', "Points")
        
    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "remove_doubles", text="Remove Doubles")

        row = layout.row()
        row.enabled = self.remove_doubles
        row.prop(self, "merge_distance", text="Merge Distance")
    
    def update(self):
        node = self.get_linked_node(0)
        if node is not None:
            print(node.outputs[0].points)
