from bpy.props import IntProperty
from .point_socket import CM_PointProperty
from ..preferences import getUserPreferences
import bpy

class CM_AgentProperty(bpy.types.PropertyGroup):    
    simulated : bpy.props.BoolProperty(name="Simulate", default=False)
    sim_start : IntProperty(name="sim start", default=0)
    sim : bpy.props.CollectionProperty(name="Sim", type=CM_PointProperty)

class CM_AgentSocket(bpy.types.NodeSocket):
	'''Agent Node Socket Type'''
	bl_idname = 'CM_AgentSocketType'
	bl_label = 'Agent Socket'

	agents : bpy.props.CollectionProperty(name="Agents", type=CM_AgentProperty)
    
	def draw(self, context, layout, node, text):
		label = text
		if self.is_linked:
			for i in self.node.inputs:
				pass
				
		layout.label(text=label)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.agent_node_color
		return (color[0], color[1], color[2], 1)