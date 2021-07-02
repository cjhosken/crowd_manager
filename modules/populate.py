from modules.agent import Agent
from bpy.types import Operator
import bpy

class CrowdManager_OT_Populate(Operator):
    bl_label = "Populate Agents"
    bl_idname = "crowdmanager.populate"
    bl_description = "Populates all agent empties with collection objects."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        crowd_collection = getCrowdCollection()

        if len(crowd_collection.objects) > 0:
            for a in crowd_collection.objects:
                bpy.data.objects.remove(a, do_unlink=True)


        control_collection = Agent.getAgentCollection()
        agent_collection = context.scene.crowdmanager_props.agent_collection

        if len(control_collection.objects) > 0:
            idx = 0
            l = 0
            for empty in control_collection.objects:
                base = agent_collection.objects[idx]
                lk = bpy.data.objects.new(empty.name + "_" + base.name, base.data)
                addInstanceToCollection(lk, crowd_collection)
                lk.location = empty.location
                lk.rotation_euler = empty.rotation_euler
                lk.scale = empty.scale
                lk.parent = empty

                if idx >= len(agent_collection.objects):
                    idx = 0
                    l += 1

        return {'FINISHED'}


class CrowdManager_OT_DePopulate(Operator):
    bl_label = "Populate Agents"
    bl_idname = "crowdmanager.depopulate"
    bl_description = "DePopulates all populated Agents"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        crowd_collection = getCrowdCollection()


        if len(crowd_collection.objects) > 0:
            for a in crowd_collection.objects:
                bpy.data.objects.remove(a, do_unlink=True)

        return {'FINISHED'}


def addInstanceToCollection(instance, col):
    if len(col.objects) > 0:
        for a in col.objects:
            if a.name == instance.name:
                bpy.data.objects.remove(a, do_unlink=True)
                break

    col.objects.link(instance)

        
def getCrowdCollection():
    collection = bpy.data.collections.get("GRP_CrowdCollection")

    if collection is None:
        collection = bpy.data.collections.new("GRP_CrowdCollection")
        bpy.context.scene.collection.children.link(collection)
            
    return collection