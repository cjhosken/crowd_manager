from modules.agent import Agent
from bpy.types import Operator

class CrowdManager_OT_Populate(Operator):
    bl_label = "Populate Agents"
    bl_idname = "crowdmanager.populate"
    bl_description = "Populates all agent empties with collection objects."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        col = Agent.getAgentCollection()
        if len(col.children) == 0:
            return {'CANCELLED'}
        else:
            return {'FINISHED'}