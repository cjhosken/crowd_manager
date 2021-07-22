import bpy
from bpy.props import *
import json
from ..base_node import CM_BaseNode

class CM_ScriptReaderNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_ScriptReaderNode'
    bl_label = 'Script Reader'
    bl_width_default = 300

    node_type = ["behavior"]

    def init(self, context):
        super().__init__()
        self.inputs.new('CM_BehaviorSocketType', "Behavior")

    def draw_buttons(self, context, layout):
        node = self.get_input_node(0)
        
        if node is not None:
            box = layout.box()
            words = node.outputs[0].code.split("\n")
            for i in range(len(words)):
                box.label(text=words[i])
 
