import bpy
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_ObjectInputNode(bpy.types.Node, CM_BaseNode):
    '''Object Input Node'''
    bl_idname = 'CM_ObjectInputNode'
    bl_label = 'Object'

    node_type = ["object"]

    ref_object : PointerProperty(
        name="Object",
        type=bpy.types.Object,
        update = CM_BaseNode.property_changed
    )
    
    def init(self, context):
        super().__init__()
        self.outputs.new('CM_ObjectSocketType', "Object")

    def draw_buttons(self, context, layout):
        layout.prop(self, "ref_object")
    
    def edit(self):
        self.outputs[0].object = self.ref_object
        self.linked_update()