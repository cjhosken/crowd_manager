import bpy
from bpy.types import Collection, NodeSocket
from ..preferences import getUserPreferences


class CrowdManager_CollectionSocket(NodeSocket):
	bl_idname = 'CrowdManager_CollectionSocketType'
	bl_label = 'Collection Socket'

	collection : bpy.props.PointerProperty(type=Collection)
    
	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.collection_node_color
		return (color[0], color[1], color[2], 1)