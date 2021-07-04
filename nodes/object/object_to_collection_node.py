import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode


class CrowdManager_ObjectToCollectionNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = "CrowdManager_ObjectToCollectionNode"
    bl_label = "Object To Collection"

    node_type = "collection"

    referenced_collection: PointerProperty(type=bpy.types.Collection, name="Object", update = CrowdManagerBaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")
        self.inputs.new('CrowdManager_CollectionSocketType', "Collection")

        self.outputs.new('CrowdManager_CollectionSocketType', "Collection")

    def draw_buttons(self, context, layout):
        layout.use_property_split = True
        row = layout.row()

        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)
        if node0 is not None and node0.outputs[0].object is not None:
            if node1 is None:
                row.prop(self, "referenced_collection")
                row.operator("crowdmanager.create_collection", text="", icon='PLUS').collection_name = "GRP_" + node0.outputs[0].object.name

    def execute(self, crowd, input_node):
        pass

    def edit(self):
        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)

        if node1 is not None and node1.outputs[0].collection is not None:
            output_collection = node1.outputs[0].collection
        elif self.referenced_collection is not None:
            output_collection = self.referenced_collection
        else:
            output_collection = None

        if node0 is not None:
            ob = node0.outputs[0].object
            if ob is not None:
                if len(ob.users_collection) > 0:
                    current_collection = ob.users_collection[-1]
                else:
                    current_collection = None
                
                if output_collection is not None:
                    if current_collection is not None:
                        current_collection.objects.unlink(ob)
                    output_collection.objects.link(ob)

        if len(self.outputs) > 0:
            self.outputs[0].collection = output_collection
        
        self.link_update()
