import bpy
import json
from bpy.types import Node, Operator
from ..base_node import CrowdManager_BaseNode

class CrowdManager_BehaviorReaderNode(Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_BehaviorReaderNode'
    bl_label = 'Behavior Reader'
    bl_width_default = 350

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_BehaviorSocketType', "Behavior")

    def draw_buttons(self, context, layout):
        node = self.get_input_node(0)
        row = layout.row()
        row = row.split(factor=0.90)
        
        if node is not None:
            lines = node.outputs[0].code.split("\n")
            col = row.column()
            for line in lines:
                col.label(text=line)
        
            row.operator("crowdmanager.savebehavior", text="", icon="FILEBROWSER").node_data = self.node_id
 
class CrowdManager_OT_SaveBehavior(Operator):
    bl_label = "Save Behavior"
    bl_idname = "crowdmanager.savebehavior"
    bl_description = "saves behavior"
    bl_options = {"REGISTER", "UNDO"}

    node_data : bpy.props.StringProperty(name="Node", default="")

    def execute(self, context):
        data = json.loads(self.node_data)
        return {'FINISHED'}
