import bpy
from bpy.props import BoolProperty, StringProperty
from ..base_node import CrowdManager_BaseNode

class CrowdManager_AgentNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_AgentNode'
    bl_label = 'Agents'

    node_types = ["agent"]

    simulated : BoolProperty(default=False)

    code : StringProperty(default="")

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_BehaviorSocketType', "Behavior")
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.outputs.new('CrowdManager_AgentSocketType', "Agents")

    def draw_buttons(self, context, layout):
        node0 = self.get_input_node(0)
        node1 = self.get_input_node(1)
        if not self.simulated:
            if node0 is None or node1 is None or len(node1.outputs[0].points) < 1 or len(node0.outputs[0].code) < 1:
                layout.enabled = False
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

            for point in points:
                agent = agents.add()
                agent.sim_start = bpy.context.scene.frame_start
                agent.simulated = False
                agent_point = agent.sim.add()
                agent_point.location = point.location
                agent_point.rotation = point.rotation