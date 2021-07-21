from bgl import GL_POINT
import bpy
from bpy.props import *
from ..base_node import CM_BaseNode
from ...sockets.agent_socket import CM_AgentProperty

class CM_AgentViewerNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_AgentViewerNode'
    bl_label = 'Agent Viewer'
    bl_width_default = 150

    node_type = ["agent", "viewer"]

    GL_COLOR : FloatVectorProperty(subtype="COLOR", size=4, default=(0.75, 0.75, 0.75, 1), min=0, soft_min=0, max=1, soft_max=1, update=CM_BaseNode.property_changed)
    
    GL_AGENTS : bpy.props.CollectionProperty(name="Agents", type=CM_AgentProperty)

    def init(self, context):
        super().__init__()
        self.inputs.new("CM_AgentSocketType", "Agents")

    def draw_buttons(self, context, layout):
        col = layout.column()
        node = self.get_input_node(idx=0)
        if node is not None:
            agents = node.outputs[0].agents
            col = col.split(factor=min(0.05 + 0.05*len(agents), 0.3))
            col.label(text=str(len(agents)))
        col.prop(self, "GL_COLOR", text="")

    def edit(self):
        node = self.get_input_node(idx=0)
        self.GL_AGENTS.clear()
        if node is not None:
            for a in node.outputs[0].agents:
                ag = self.GL_AGENTS.add()
                ag.simulated = a.simulated
                ag.sim_start = a.sim_start
                for s in a.sim:
                    x = ag.sim.add()
                    x.location = s.location
