import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...agent import CrowdManager_Agent as Agent

class CrowdManager_CrowdNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_CrowdNode'
    bl_label = 'Crowd'

    node_type = "crowd"

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_BehaviorSocketType', "Behavior")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_CrowdSocketType', "Crowd")

    def draw_buttons(self, context, layout):
        pass
    
    def update(self):
        node_bh = self.get_linked_node(0)
        node_pn = self.get_linked_node(1)


        pnts = []
        if node_pn is not None and len(node_pn.output[0].points) > 0:
            pnts = node_pn.output[0].points
        
        

        


            


        