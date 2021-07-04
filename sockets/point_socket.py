from .. import point
import bpy
from bpy.props import BoolProperty, CollectionProperty, PointerProperty
from ..preferences import getUserPreferences
from .utils import updateParameter

class CrowdManager_PointSocket(bpy.types.NodeSocket):
	'''Point Node Socket Type'''
	bl_idname = 'CrowdManager_PointSocketType'
	bl_label = 'Point Socket'

	#points : CollectionProperty(type=CrowdManager_Point, update=updateParameter)

	# points need location and rotation vectors (make your own property)

	def draw(self, context, layout, node, text):
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.point_node_color
		return (color[0], color[1], color[2], 1)
