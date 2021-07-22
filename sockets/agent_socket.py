from bpy.props import IntProperty, BoolProperty, CollectionProperty
from bpy.types import PropertyGroup, NodeSocket
from .point_socket import CrowdManager_PointProperty
from ..preferences import getUserPreferences

class CrowdManager_AgentProperty(PropertyGroup):    
    simulated : BoolProperty(name="Simulate", default=False)
    sim_start : IntProperty(name="sim start", default=0)
    sim : CollectionProperty(name="Sim", type=CrowdManager_PointProperty)

class CrowdManager_AgentSocket(NodeSocket):
	'''Agent Node Socket Type'''
	bl_idname = 'CrowdManager_AgentSocketType'
	bl_label = 'Agent Socket'

	agents : CollectionProperty(name="Agents", type=CrowdManager_AgentProperty)
    
	def draw(self, context, layout, node, text):				
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.agent_node_color
		return (color[0], color[1], color[2], 1)