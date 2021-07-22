import bpy
import json
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_ScriptBehaviorNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_ScriptBehaviorNode'
    bl_label = 'Script Behavior'
    bl_width_default = 150

    script : bpy.props.PointerProperty(type=bpy.types.Text)

    node_type = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CM_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "script", text="")
        row.operator("crowdmanager.refreshnode", text="", icon="FILE_REFRESH").node_data = self.node_id
    
    def edit(self):
        code = ""
        if self.script is not None:
            for l in self.script.lines:
                code += l.body +"\n"

        self.outputs[0].code = code
        
        self.linked_update()

class CM_RefreshNode(bpy.types.Operator):
    bl_label = "Refresh Node"
    bl_idname = "crowdmanager.refreshnode"
    bl_description = "Refreshes node."
    bl_options = {"REGISTER", "UNDO"}

    node_data : bpy.props.StringProperty(name="Node", default="")

    def execute(self, context):
        data = json.loads(self.node_data)
        node = bpy.data.node_groups[data[1]].nodes[data[0]]
        node.edit()
        return {'FINISHED'}