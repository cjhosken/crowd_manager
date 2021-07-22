import bpy
from bpy.types import Node, Object
from ..base_node import CrowdManager_BaseNode

class CrowdManager_ObjectInputNode(Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_ObjectInputNode'
    bl_label = 'Object'

    node_types = ["object"]

    object : bpy.props.PointerProperty(
        name="Object",
        description="Object input",
        type=Object,
        update = CrowdManager_BaseNode.property_changed
    )
    
    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_ObjectSocketType', "Object")

    def draw_buttons(self, context, layout):
        layout.prop(self, "object", text="")
    
    def edit(self):
        self.outputs[0].object = self.object
        self.linked_update()
    
    def free(self):
        self.outputs[0].object = None
        self.linked_update()