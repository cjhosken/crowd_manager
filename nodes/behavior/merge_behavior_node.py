import bpy
import json
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_MergeBehaviorNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_MergeBehaviorNode'
    bl_label = 'Merge Behavior'
    bl_width_default = 150

    mix : bpy.props.FloatProperty(default=0.5, min=0, max=1, update=CM_BaseNode.property_changed)

    node_type = ["behavior"]

    def init(self, context):
        super().__init__()
        self.inputs.new("CM_BehaviorSocketType", "Behavior")
        self.inputs.new("CM_BehaviorSocketType", "Behavior")
        self.outputs.new("CM_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "mix", text="")
    
    def edit(self):
        code = ""
        node0 = self.get_input_node(0)
        node1 = self.get_input_node(1)
        
        if node0 is None:
            if node1 is not None:
                code = node1.outputs[0].code
        else:
            if node1 is None:
                code = node0.outputs[0].code
            
            else:
                code0 = node0.outputs[0].code
                code0_split = code0.split("\n")
                for idx, line in enumerate(code0_split):
                    code0_split[idx] = "    " + line
                code0 = "\n".join(code0_split)

                code1 = node1.outputs[0].code
                code1_split = code1.split("\n")
                for idx, line in enumerate(code1_split):
                    code1_split[idx] = "    " + line
                code1 = "\n".join(code1_split)

                func_name = (self.name).replace(" ", "")
                func_tree = (self.id_data.name).replace(" ", "")
                func_label = f"{func_name}_{func_tree}"

                code = f"""
def {func_label}_m0():
    {code0}
    return OUTPUT

def {func_label}_m1():
    {code1}
    return OUTPUT

OUT0 = {func_label}_m0()
OUT1 = {func_label}_m1()
MIX = {self.mix}

LOCATION = [
    OUT0[0][0] * (1 - MIX) + OUT1[0][0] * MIX,
    OUT0[0][1] * (1 - MIX) + OUT1[0][1] * MIX,
    OUT0[0][2] * (1 - MIX) + OUT1[0][2] * MIX
]

ROTATION = [
    OUT0[1][0] * (1 - MIX) + OUT1[1][0] * MIX,
    OUT0[1][1] * (1 - MIX) + OUT1[1][1] * MIX,
    OUT0[1][2] * (1 - MIX) + OUT1[1][2] * MIX
]

OUTPUT = [LOCATION, ROTATION]    
                """
        self.outputs[0].code = code
        
        self.linked_update()