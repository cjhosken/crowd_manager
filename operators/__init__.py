import bpy
from bpy.props import BoolProperty, StringProperty
from bpy.types import Operator

class CrowdManager_OT_CreateCollection(Operator):
    bl_label = "Create Collection"
    bl_idname = "crowdmanager.create_collection"
    bl_description = "Creates a collection"
    bl_options = {"REGISTER", "UNDO"}

    collection_name : StringProperty(name="Collection Name")

    def execute(self, context):
        collection = bpy.data.collections.get(self.collection_name)

        if collection is None:
            collection = bpy.data.collections.new(self.collection_name)
            bpy.context.scene.collection.children.link(collection)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

operator_classes = [CrowdManager_OT_CreateCollection]