import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.agent import CM_Agent, CM_AgentList
from ...types.point import CM_Point, CM_PointList

class CrowdManager_AgentNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_AgentNode'
    bl_label = 'Agents'

    node_type = "agent"

    linked : BoolProperty()
    agents : bpy.props.StringProperty(name="Points", default=CM_AgentList().toJSON())

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_BehaviorSocketType', "Behavior")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_AgentSocketType', "Agents")

    def draw_buttons(self, context, layout):
        layout.operator("crowdmanager.simulate", text='Simulate', icon='BOIDS').agents = self.outputs[0].agents
    
    def edit(self):
        self.agents = CM_AgentList().toJSON()
        agents = CM_AgentList(dict=CM_AgentList.fromJSON(self.agents))

        node1 = self.get_linked_node(1)
        node0 = self.get_linked_node(0)
        code = ""
        if node1 is not None:
            points = CM_PointList(dict=CM_PointList.fromJSON(node1.outputs[0].points))

            if node0 is not None:
                code = node0.outputs[0].code

            for p in points.points:
                ag = CM_Agent(p, code=code)
                agents.add(ag)
        
        self.outputs[0].agents = agents.toJSON()
        self.link_update()

    def update(self):
        for i in self.inputs:
            if i.links:
                if not self.linked:
                    self.edit()
                    self.linked = True
            else:
                if self.linked:
                    self.edit()
                    self.linked = False