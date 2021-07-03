import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_CollectionToObjectNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = "CrowdManager_CollectionToObjectNode"
    bl_label = "Collection To Object"

    node_type = "object"

    collection_object: PointerProperty(type=bpy.types.Object, name="Object")

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_CollectionSocketType', "Collection")
        self.outputs.new('CrowdManager_ObjectSocketType', "Object")
    
    def draw_buttons(self, context, layout):
        layout.use_property_split = True
        col = layout.column()
        
        node = self.get_linked_node(0)
        if node is not None and node.outputs[0].collection is not None:
            col.prop_search(self, "collection_object", node.outputs[0].collection, "objects")
            
            
    def execute(self, crowd, input_node):
        pass

    def update(self):
        if len(self.outputs) > 0:
            self.outputs[0].object = self.collection_object
        self.link_update()