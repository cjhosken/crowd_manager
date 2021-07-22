import bpy
import json
from bpy.props import PointerProperty, StringProperty
from bpy.types import Node, Text, Operator
from ..base_node import CrowdManager_BaseNode

class CrowdManager_ScriptBehaviorNode(Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_ScriptBehaviorNode'
    bl_label = 'Script Behavior'
    bl_width_default = 150

    script : PointerProperty(type=Text)

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "script", text="")
        row.operator("crowdmanager.refreshnode", text="", icon="FILE_REFRESH").node_data = self.node_id
    
    def edit(self):
        code = ""
        if self.script is not None:
            for line in self.script.lines:
                code += line.body +"\n"

        self.outputs[0].code = code
        
        self.linked_update()

class CrowdManager_OT_NodeRefresh(Operator):
    bl_label = "Refresh"
    bl_idname = "crowdmanager.refreshnode"
    bl_description = "refreshes script"
    bl_options = {"REGISTER", "UNDO"}

    node_data : StringProperty(name="Node", default="")

    def execute(self, context):
        data = json.loads(self.node_data)
        node = bpy.data.node_groups[data[1]].nodes[data[0]]
        node.edit()
        return {'FINISHED'}