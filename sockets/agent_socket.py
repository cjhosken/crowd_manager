import bpy
from bpy.props import BoolProperty
from ..preferences import getUserPreferences
from .utils import updateParameter

class CrowdManager_AgentSocket(bpy.types.NodeSocket):
    '''Agent Node Socket Type'''
    bl_idname = 'CrowdManager_AgentSocketType'
    bl_label = 'Agent Socket'

    agents : bpy.props.StringProperty(name="Agents", default='{"agents" : []}', update=updateParameter)

    def draw(self, context, layout, node, text):
        layout.label(text=text)

    def draw_color(self, context, node):
        prefs = getUserPreferences(context)
        color = prefs.agent_node_color
        return (color[0], color[1], color[2], 1)
