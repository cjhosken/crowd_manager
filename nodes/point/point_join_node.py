import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_PointJoinNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointJoinNode'
    bl_label = 'Join Points'

    node_type = "point"

    #remove_doubles : BoolProperty(default=False, update = CrowdManagerBaseNode.property_changed)
    #merge_distance : FloatProperty(default = 0.001, update = CrowdManagerBaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_PointSocketType', "Points")
        
    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)

        self.link_update()
        

        
