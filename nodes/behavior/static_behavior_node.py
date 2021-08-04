import bpy
from ..base_node import CrowdManager_BaseNode

class CrowdManager_StaticBehaviorNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_StaticBehaviorNode'
    bl_label = 'Static Behavior'
    bl_width_default = 150

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()

        self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        code = """
LOCATION = LAST_SIM.location

ROTATION = LAST_SIM.rotation

OUTPUT = [LOCATION, ROTATION]    
                """
        self.outputs[0].code = code
        
        self.linked_update()