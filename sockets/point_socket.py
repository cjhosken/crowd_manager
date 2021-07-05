import bpy
import threading
import math
from ..preferences import getUserPreferences
from .utils import updateParameter, updatePointNodeSocketValue
from ..types.point import CM_Point, CM_PointList

class CrowdManager_PointSocket(bpy.types.NodeSocket):
	'''Point Node Socket Type'''
	bl_idname = 'CrowdManager_PointSocketType'
	bl_label = 'Point Socket'

	points : bpy.props.StringProperty(name="Points", description="List of CrowdManager points", default=CM_PointList().toJSON(), update=updateParameter)

	def draw(self, context, layout, node, text):
		label = text
		if self.is_linked:
			for i in self.node.inputs:
				pass
				
		layout.label(text=label)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.point_node_color
		return (color[0], color[1], color[2], 1)
