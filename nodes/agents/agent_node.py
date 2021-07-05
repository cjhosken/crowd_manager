import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types import CrowdManager_Agent as CM_Agent

class CrowdManager_AgentNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_AgentNode'
    bl_label = 'Agents'

    node_type = "agent"

    agents = {"agents" : [], "simulated" : False}
    code = ""

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_BehaviorSocketType', "Behavior")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_AgentSocketType', "Agents")

    def draw_buttons(self, context, layout):
        layout.operator("crowdmanager.simulate", text='Simulate', icon='BOIDS').agents = self.outputs[0].agents
    
    def edit(self):
        node_bh = self.get_linked_node(0)
        node_pn = self.get_linked_node(1)
        
        if node_pn is None:
            agents = {"agents" : [], "simulated" : False}

        if node_pn is not None and len(json.loads(node_pn.outputs[0].points)["points"]) > 0:
            CM_Agent.clearAgentCollection(CM_Agent.getAgentCollection())
            pnts = json.loads(node_pn.outputs[0].points)["points"]

            if node_bh is not None:
                self.code = node_bh.outputs[0].code

            for i, p in enumerate(pnts):
                ag = CM_Agent(self.code, p, i)
                self.agents["agents"].append(ag.toDict())

        elif node_pn is None or len(json.loads(node_pn.outputs[0].points)["points"]) <= 0:
            CM_Agent.clearAgentCollection(CM_Agent.getAgentCollection())
            agents = {"agents" : [], "simulated" : False}

        self.outputs[0].agents = json.dumps(self.agents)

    def update(self):
        self.link_update()