from ..preferences import getUserPreferences
import bpy

class CM_BehaviorSocket(bpy.types.NodeSocket):
	'''Behavior Node Socket Type'''
	bl_idname = 'CM_BehaviorSocketType'
	bl_label = 'Behavior Socket'

	code : bpy.props.StringProperty(name="Code", default="")
    
	def draw(self, context, layout, node, text):
		label = text
		if self.is_linked:
			for i in self.node.inputs:
				pass
				
		layout.label(text=label)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.behavior_node_color
		return (color[0], color[1], color[2], 1)