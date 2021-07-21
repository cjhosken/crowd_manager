import bpy
from bpy.props import *
import json
from ..base_node import CM_BaseNode

class CM_AgentNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_AgentNode'
    bl_label = 'Agents'

    node_type = ["agent"]

    simulated : BoolProperty(default=False)

    node_id : StringProperty(default="")

    code : StringProperty(default="")

    def init(self, context):
        super().__init__()
        self.inputs.new('CM_BehaviorSocketType', "Behavior")
        self.inputs.new('CM_PointSocketType', "Points")

        self.outputs.new('CM_AgentSocketType', "Agents")

    def draw_buttons(self, context, layout):
        pass
        if not self.simulated:
            layout.operator("crowdmanager.simulate", text='Simulate', icon='BOIDS').node_data = self.node_id
        else:
            layout.operator("crowdmanager.desimulate", text='Clear Simulation', icon='X').node_data = self.node_id
    
    def edit(self):
        self.simulated = False
        agents = self.outputs[0].agents
        agents.clear()

        node1 = self.get_input_node(1)
        node0 = self.get_input_node(0)

        if node1 is not None:
            points = node1.outputs[0].points

            if node0 is not None:
                self.code = node0.outputs[0].code

            for p in points:
                ag = agents.add()
                x = ag.sim.add()
                x.location = p.location

        self.node_id = json.dumps([str(self.name), str(self.id_data.name)])