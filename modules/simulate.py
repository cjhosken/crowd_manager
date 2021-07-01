import bpy
from bpy.types import Operator

class CrowdManager_OT_Simulate(Operator):
    bl_label = "Simulate Crowds"
    bl_idname = "crowdmanager.simulate"
    bl_description = "Simulates crowd agents."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        agents = []
        context.scene.frame_set(context.scene.frame_start)
        for a in agents:
            a.reset()

        while context.scene.frame_current <= context.scene.frame_end:
            print(context.scene.frame_current)
            for a in agents:
                a.update()
            
            context.scene.frame_set(context.scene.frame_current + 1)

        return {'FINISHED'}
