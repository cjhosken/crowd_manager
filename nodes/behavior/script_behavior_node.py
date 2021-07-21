import bpy
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_ScriptBehaviorNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_ScriptBehaviorNode'
    bl_label = 'Script Behavior'
    bl_width_default = 150

    script : bpy.props.PointerProperty(type=bpy.types.Text)
    button : bpy.props.BoolProperty(default = False, update=CM_BaseNode.property_changed)

    node_type = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CM_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        layout.prop(self, "script", text="")
        layout.prop(self, "button")
    
    def edit(self):
        code = ""
        if self.script is not None:
            for l in self.script.lines:
                code += l.body +"\n"

        self.outputs[0].code = code
        
        self.linked_update()
        