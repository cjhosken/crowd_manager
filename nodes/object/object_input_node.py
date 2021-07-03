import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_ObjectInputNode(bpy.types.Node, CrowdManagerBaseNode):
    '''Object Input Node'''
    bl_idname = 'CrowdManager_ObjectInputNode'
    bl_label = 'Object'

    node_type = "object"

    ref_object : PointerProperty(
        name="Object",
        type=bpy.types.Object,
        update = CrowdManagerBaseNode.property_changed
    )
    
    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_ObjectSocketType', "Object")

    def draw_buttons(self, context, layout):
        layout.prop(self, "ref_object")
    
    def update(self):
        self.outputs[0].object = self.ref_object