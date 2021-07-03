import bpy
from bpy.props import *

class CrowdManager_Preferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    use_node_colors : BoolProperty(
        name="Use Node Colors",
        description="Use node body colors",
        default=False,
    )

    node_saturation : FloatProperty(
        name="Node Saturation",
        description="Saturation of node body colors",
        default = 0.7,
        min=0, max=1
    )

    object_node_color : FloatVectorProperty(
        name="Object Nodes Color",
        subtype="COLOR",
        default=(1, .7, .2),
        min=0, max=1
    )

    collection_node_color : FloatVectorProperty(
        name="Collection Nodes Color",
        subtype="COLOR",
        default=(1, .5, .3),
        min=0, max=1
    )

    point_node_color : FloatVectorProperty(
        name="Point Nodes Color",
        subtype="COLOR",
        default=(.7, .7, .7),
        min=0, max=1
    )

    behavior_node_color : FloatVectorProperty(
        name="Behavior Nodes Color",
        subtype="COLOR",
        default=(.4, .8, .2),
        min=0, max=1
    )

    agent_node_color : FloatVectorProperty(
        name="Agent Nodes Color",
        subtype="COLOR",
        default=(.6, .3, .7),
        min=0, max=1
    )

    crowd_node_color : FloatVectorProperty(
        name="Crowd Nodes Color",
        subtype="COLOR",
        default=(.1, .3, .7),
        min=0, max=1
    )

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        subcol = col.split()
        subcolcol = subcol.column()
        subcolcol.prop(self, "use_node_colors")
        subcolcolrow = subcolcol.row()
        subcolcolrow.enabled = self.use_node_colors
        subcolcolrow.prop(self, "node_saturation")
        subcol.prop(self, "object_node_color")
        subcol.prop(self, "collection_node_color")
        subcol.prop(self, "point_node_color")
        subcol.prop(self, "behavior_node_color")
        subcol.prop(self, "agent_node_color")
        subcol.prop(self, "crowd_node_color")

        col = layout.column()
        col.operator("wm.url_open", text="Report Bug", icon='URL').url = "https://github.com/Christopher-Hosken/crowdManager/issues"

classes = [CrowdManager_Preferences]

def getUserPreferences(context=None):
	if not context:
		context = bpy.context
	prefs = None
	if hasattr(context, "user_preferences"):
		prefs = context.user_preferences.addons.get(__package__, None)
	elif hasattr(context, "preferences"):
		prefs = context.preferences.addons.get(__package__, None)
	if prefs:
		return prefs.preferences
	return None

def desaturate(c, f=0.5):
    f = (1 - f)
    L = 0.3*c[0] + 0.6*c[1] + 0.1*c[2]

    return (
        c[0] + f * (L - c[0]),
        c[1] + f * (L - c[1]),
        c[2] + f * (L - c[2]),
    )