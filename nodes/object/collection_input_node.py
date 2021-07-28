
import bpy
from bpy.types import Node, Collection
from ..base_node import CrowdManager_BaseNode

class CrowdManager_CollectionInputNode(Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_CollectionInputNode'
    bl_label = 'Collection'

    node_type = "collection"

    ref_collection : bpy.props.PointerProperty(
        name="Collection",
        type=Collection,
        update = CrowdManager_BaseNode.property_changed
    )
    
    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_CollectionSocketType', "Collection")

    def draw_buttons(self, context, layout):
        layout.prop(self, "ref_collection", text="")
    
    def edit(self):
        self.outputs[0].collection = self.ref_collection
        self.linked_update()