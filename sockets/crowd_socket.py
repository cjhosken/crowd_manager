import bpy
from bpy.props import *
from ..preferences import getUserPreferences
from .utils import updateParameter

class CrowdManager_CrowdSocket(bpy.types.NodeSocket):
	'''Crowd Node Socket Type'''
	bl_idname = 'CrowdManager_CrowdSocketType'
	bl_label = 'Crowd Socket'

	crowd_collection : PointerProperty(type=bpy.types.Collection, update=updateParameter)

	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.crowd_node_color
		return (color[0], color[1], color[2], 1)
