import bpy
from ..preferences import getUserPreferences
from .utils import updateParameter

class CrowdManager_BehaviorSocket(bpy.types.NodeSocket):
	'''Behavior Node Socket Type'''
	bl_idname = 'CrowdManager_BehaviorSocketType'
	bl_label = 'Behavior Socket'

	code : bpy.props.StringProperty(default="pass")

	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.behavior_node_color
		return (color[0], color[1], color[2], 1)
