import bpy
from ..preferences import getUserPreferences
from .utils import updateParameter

class CrowdManager_ObjectSocket(bpy.types.NodeSocket):
	'''Object Node Socket Type'''
	bl_idname = 'CrowdManager_ObjectSocketType'
	bl_label = 'Object Socket'

	object : bpy.props.PointerProperty(name="Object", type=bpy.types.Object, update=updateParameter)

	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.object_node_color
		return (color[0], color[1], color[2], 1)
