import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_CrowdOutputNode(bpy.types.Node, CrowdManagerBaseNode):
    '''Crowd Output Node'''
    bl_idname = 'CrowdManager_CrowdOutputNode'
    bl_label = 'Output'

    node_type = "crowd"

    crowd_collection : bpy.props.PointerProperty(type=bpy.types.Collection)
    
    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_CrowdSocketType', "Crowd")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "crowd_collection", text="")
        row.operator("crowdmanager.create_collection", text="", icon='PLUS').collection_name = "CROWD_Crowd"
    
    def update(self):
        pass