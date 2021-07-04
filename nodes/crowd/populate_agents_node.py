import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...sockets.utils import string_to_list

class CrowdManager_PopulateAgentsNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PopulateAgentsNode'
    bl_label = 'Populate Agents'

    node_type = "crowd"

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_AgentSocketType', "Agents")
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")

        self.outputs.new('CrowdManager_CrowdSocketType', "Crowd")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        node0 = self.get_linked_node(0)
        if node0 is not None:
            print(string_to_list(node0.outputs[0].agents))
        


        


            


        