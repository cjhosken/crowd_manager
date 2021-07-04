import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

class CrowdManager_WanderBehaviorNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_WanderBehaviorNode'
    bl_label = 'Wander Behavior'

    node_type = "behavior"
    
    code = """\n
        import random
        self._loc[0] += random.random()
        self._loc[1] += random.random()
        """


    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_BehaviorSocketType', "Behavior")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        self.outputs[0].code = self.code