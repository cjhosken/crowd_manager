import bpy
from bpy.types import AddonPreferences
from bpy.props import BoolProperty, FloatProperty, FloatVectorProperty


class CrowdManager_Preferences(AddonPreferences):
    bl_idname = __package__

    use_node_colors: BoolProperty(
        name="Use Node Colors",
        default=False
    )

    node_saturation: FloatProperty(
        name="Node Saturation",
        default=0.7,
        min=0, max=1
    )

    object_node_color: FloatVectorProperty(
        name="Object Node Color",
        subtype="COLOR",
        default=(1, 0.7, 0.2),
        min=0, max=1
    )

    collection_node_color: FloatVectorProperty(
        name="Collection Node Color",
        subtype="COLOR",
        default=(1, 0.5, 0.3),
        min=0, max=1
    )

    point_node_color: FloatVectorProperty(
        name="Point Node Color",
        subtype="COLOR",
        default=(0.6, 0.7, 0.9),
        min=0, max=1
    )

    behavior_node_color: FloatVectorProperty(
        name="Behavior Node Color",
        subtype="COLOR",
        default=(0.3, 0.7, 0.3),
        min=0, max=1
    )

    agent_node_color: FloatVectorProperty(
        name="Agent Node Color",
        subtype="COLOR",
        default=(0.6, 0.3, 0.7),
        min=0, max=1
    )

    crowd_node_color: FloatVectorProperty(
        name="Crowd Node Color",
        subtype="COLOR",
        default=(0.1, 0.3, 0.7),
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
        col.operator("wm.url_open", text="Report Bug",
                     icon='URL').url = "https://github.com/Christopher-Hosken/crowdManager/issues"


classes = [CrowdManager_Preferences]


def getUserPreferences(context=None):
    if not context:
        context = bpy.context

    if hasattr(context, "user_preferences"):
        prefs = context.user_preferences.addons.get(__package__, None)
    elif hasattr(context, "preferences"):
        prefs = context.preferences.addons.get(__package__, None)
    if prefs:
        return prefs.preferences
    return None


def desaturate(c, f=0.5):
    f = (1-f)
    L = 0.3*c[0] + 0.6*c[1] + 0.1*c[2]

    return (
        c[0] + f * (L - c[0]),
        c[1] + f * (L - c[1]),
        c[2] + f * (L - c[2]),
    )