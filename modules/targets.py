import bpy
from bpy.props import FloatProperty, IntProperty, PointerProperty
from bpy.types import Operator

class CrowdManager_OT_AddTarget(Operator):
    bl_label = "Add Targets"
    bl_idname = "crowdmanager.add_target"
    bl_description = "Adds target object."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        context.scene.crowdmanager_targets.add()
        return {'FINISHED'}

class CrowdManager_OT_DeleteTarget(Operator):
    bl_label = "Add Targets"
    bl_idname = "crowdmanager.del_target"
    bl_description = "Delete target object."
    bl_options = {"REGISTER", "UNDO"}

    index : IntProperty(
        name="index",
        min=0,
        default = 0
    )

    def execute(self, context):
        context.scene.crowdmanager_targets.remove(self.index)
        return {'FINISHED'}

class CROWDMANAGER_TargetCollection(bpy.types.PropertyGroup):
    object : PointerProperty(
        type= bpy.types.Object,
        name="Target Object",
        description="Target object for agents.",
    )

    attraction : FloatProperty(
        name="Attraction",
        description="Amount of attraction an agent has to a target.",
        min=-1,
        max=1,
        default = 0,
    )

    max_distance : FloatProperty(
        name="Attraction distance threshold",
        description="Distance threshold in which agents become attracted to a target.",
        min=0,
        default = 10.0,
    )