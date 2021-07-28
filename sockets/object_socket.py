import bpy
from bpy.types import Object, NodeSocket
from ..preferences import getUserPreferences


class CrowdManager_ObjectSocket(NodeSocket):
	bl_idname = 'CrowdManager_ObjectSocketType'
	bl_label = 'Object Socket'

	object : bpy.props.PointerProperty(type=Object)
    
	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.object_node_color
		return (color[0], color[1], color[2], 1)