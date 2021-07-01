from modules.agent import Agent
from bpy.types import Operator

class CrowdManager_OT_Distribute(Operator):
    bl_label = "Distribute Agents"
    bl_idname = "crowdmanager.distribute"
    bl_description = "Scatters agents across a surface."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        col = Agent.getAgentCollection()
        if len(col.children) == 0:
            return {'CANCELLED'}
        else:
            return {'FINISHED'}