import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_CollectionInputNode(bpy.types.Node, CrowdManagerBaseNode):
    '''Collection Input Node'''
    bl_idname = 'CrowdManager_CollectionInputNode'
    bl_label = 'Collection'

    node_type = "collection"

    ref_collection : PointerProperty(
        name="Collection",
        type=bpy.types.Collection,
        update = CrowdManagerBaseNode.property_changed
    )
    
    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_CollectionSocketType', "Collection")

    def draw_buttons(self, context, layout):
        layout.prop(self, "ref_collection")
    
    def update(self):
        if len(self.outputs) > 0:
            self.outputs[0].collection = self.ref_collection
        self.link_update()