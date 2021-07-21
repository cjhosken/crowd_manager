import bpy
from ..preferences import getUserPreferences

class CM_PointProperty(bpy.types.PropertyGroup):
    location : bpy.props.FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0))

class CM_PointSocket(bpy.types.NodeSocket):
	'''Point Node Socket Type'''
	bl_idname = 'CM_PointSocketType'
	bl_label = 'Point Socket'

	points : bpy.props.CollectionProperty(name="Points", type=CM_PointProperty)
    
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