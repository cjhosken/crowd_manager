from bpy.types import PropertyGroup, NodeSocket
from bpy.props import FloatVectorProperty, CollectionProperty
from ..preferences import getUserPreferences

class CrowdManager_PointProperty(PropertyGroup):
	location : FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0))
	rotation : FloatVectorProperty(name="Rotation", subtype="EULER", default=(0, 0, 0))

class CrowdManager_PointSocket(NodeSocket):
	bl_idname = 'CrowdManager_PointSocketType'
	bl_label = 'Point Socket'

	points : CollectionProperty(name="Points", type=CrowdManager_PointProperty)
    
	def draw(self, context, layout, node, text):	
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.point_node_color
		return (color[0], color[1], color[2], 1)