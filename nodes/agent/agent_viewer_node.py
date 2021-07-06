import bpy
import gpu
from gpu_extras.batch import batch_for_shader
import bgl
import math
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.point import CM_PointList, CM_Point
from ...types.agent import CM_AgentList, CM_Agent

GL_AGENTS = []

class CrowdManager_AgentViewerNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_AgentViewerNode'
    bl_label = 'Agent Viewer'

    node_type = "agent"


    linked : BoolProperty()
    agent_color : FloatVectorProperty(subtype="COLOR", size=4, default=(0.5, 0.5, 0.5, 1), min=0, soft_min=0, max=1, soft_max=1, update=CrowdManagerBaseNode.property_changed)

    def init(self, context):
        self.inputs.new('CrowdManager_AgentSocketType', "Agents")
        
    def draw_buttons(self, context, layout):
        col = layout.column()
        node0 = self.get_linked_node(0)
        if node0 is not None:
            agents = CM_AgentList(dict=CM_AgentList.fromJSON(node0.outputs[0].agents))
            col = col.split(factor=min(0.05 + 0.05*len(str(agents.agents)), 0.3))
            col.label(text=str(len(agents.agents)))
        col.prop(self, "agent_color", text="")

    def edit(self):
        node0 = self.get_linked_node(0)
        if node0 is not None:
            agents = CM_AgentList(dict=CM_AgentList.fromJSON(node0.outputs[0].agents))
                
            ac = self.agent_color
            pnt = []
            col = []

            for a in agents.agents:
                og = a.origin
                if a.simulated:
                    if bpy.context.scene.frame_current >= a.sim_start and bpy.context.scene.frame_current < a.sim_start + len(a.sim_data):
                        og = a.sim_data[bpy.context.scene.frame_current - a.sim_start]
                        

                pnt.append((og.location[0], og.location[1], og.location[2]))
                col.append((ac[0], ac[1], ac[2], ac[3]))
                

            for i, s in enumerate(GL_AGENTS):
                if str(s[0]) == self.name:
                    GL_AGENTS[i] =  [
                            self.name,
                            pnt,
                            col
                        ]
                    break
            else:
                GL_AGENTS.append([
                    self.name,
                    pnt,
                    col
                ])

    def clear_points(self):
        for i, s in enumerate(GL_AGENTS):
            if s[0] == self.name:
                GL_AGENTS.pop(i)

    def free(self):
        for i, s in enumerate(GL_AGENTS):
            if s[0] == self.name:
                GL_AGENTS.pop(i)
    
    def update(self):
        for i in self.inputs:
            if i.links:
                if not self.linked:
                    self.edit()
                    self.linked = True
            else:
                if self.linked:
                    self.edit()
                    self.clear_points()
                    self.linked = False
