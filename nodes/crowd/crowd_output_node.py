import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_CrowdOutputNode(bpy.types.Node, CrowdManagerBaseNode):
    '''Crowd Output Node'''
    bl_idname = 'CrowdManager_CrowdOutputNode'
    bl_label = 'Output'

    node_type = "crowd"
    
    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_CrowdSocketType', "Crowd")

    def draw_buttons(self, context, layout):
        layout.operator("crowdmanager.simulate", text='Simulate', icon='BOIDS')
    
    def update(self):
        pass