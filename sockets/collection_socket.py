import bpy
from ..preferences import getUserPreferences
from .utils import updateParameter

class CrowdManager_CollectionSocket(bpy.types.NodeSocket):
	'''Collection Node Socket Type'''
	bl_idname = 'CrowdManager_CollectionSocketType'	
	bl_label = 'Collection Socket'

	collection : bpy.props.PointerProperty(name="Colleciton", type=bpy.types.Collection, update=updateParameter)

	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.collection_node_color
		return (color[0], color[1], color[2], 1)
