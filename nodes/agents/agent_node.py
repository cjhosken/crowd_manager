import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...agent import Agent

class CrowdManager_AgentNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_AgentNode'
    bl_label = 'Agents'

    node_type = "agent"

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_BehaviorSocketType', "Behavior")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_AgentSocketType', "Agents")

    def draw_buttons(self, context, layout):
        layout.operator("crowdmanager.simulate", text='Simulate', icon='BOIDS')
    
    def update(self):
        node_bh = self.get_linked_node(0)
        node_pn = self.get_linked_node(1)

        agents = []
        code = ""
        if node_pn is not None and len(node_pn.outputs[0].points) > 0:
            if node_bh is not None and node_bh.outputs[0].code is not None:
                code = node_bh.outputs[0].code
            for i, p in enumerate(node_pn.outputs[0].points):
                ag = Agent(code, p)
                agents.append(ag, i)
        
        self.outputs[0].agents = []

        
        
        


        


            


        