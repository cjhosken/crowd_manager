import bpy
import json
from bpy.props import *
from ..types import CrowdManager_Agent as CM_Agent, CrowdManager_Point as CM_Point

class CrowdManager_OT_CreateCollection(bpy.types.Operator):
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

class CrowdManager_OT_Simulate(bpy.types.Operator):
    bl_label = "Simulate Crowds"
    bl_idname = "crowdmanager.simulate"
    bl_description = "Simulates crowd agents."
    bl_options = {"REGISTER", "UNDO"}

    agents : StringProperty(name="Agents")

    def execute(self, context):
        agents = json.loads(self.agents)["agents"]

        context.scene.frame_set(context.scene.frame_start + 1)

        f = 0
        e = context.scene.frame_end - (context.scene.frame_start + 1)
        while context.scene.frame_current <= context.scene.frame_end:
            for a in agents:
                ag = CM_Agent(id=a["id"], pnt=CM_Point(a["bLoc"], a["bRot"]).toDict(), code=a["code"], obname=a["obname"])
                if ag._ob is not None:
                    if context.scene.frame_current == context.scene.frame_start + 1:
                        ag.clear()
                    ag.update()
                print(f"SIMULATING FRAME {context.scene.frame_current} - {((f / e)*100):.2f}%")
            
            context.scene.frame_set(context.scene.frame_current + 1)
            f += 1
            
        context.scene.frame_set(context.scene.frame_start)
        return {'FINISHED'}


operator_classes = [CrowdManager_OT_CreateCollection, CrowdManager_OT_Simulate]