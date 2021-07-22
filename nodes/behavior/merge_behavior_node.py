import bpy
from ..base_node import CrowdManager_BaseNode

class CrowdManager_MergeBehaviorNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_MergeBehaviorNode'
    bl_label = 'Merge Behavior'
    bl_width_default = 150

    mix : bpy.props.FloatProperty(name="Merge", default=0.5, description="slider value for merge", min=0, max=1, precision=3, update=CrowdManager_BaseNode.property_changed)

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()
        self.inputs.new("CrowdManager_BehaviorSocketType", "Behavior")
        self.inputs.new("CrowdManager_BehaviorSocketType", "Behavior")
        self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, "mix", text="Fac:", slider=True)
    
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
def {func_label}_b0():
    {code0}
    return OUTPUT

def {func_label}_b1():
    {code1}
    return OUTPUT

BEHAVIOR_0 = {func_label}_b0()
BEHAVIOR_1 = {func_label}_b1()
MIX = {self.mix}

LOCATION = [
    BEHAVIOR_0[0][0] * (1 - MIX) + BEHAVIOR_1[0][0] * MIX,
    BEHAVIOR_0[0][1] * (1 - MIX) + BEHAVIOR_1[0][1] * MIX,
    BEHAVIOR_0[0][2] * (1 - MIX) + BEHAVIOR_1[0][2] * MIX
]

ROTATION = [
    BEHAVIOR_0[1][0] * (1 - MIX) + BEHAVIOR_1[1][0] * MIX,
    BEHAVIOR_0[1][1] * (1 - MIX) + BEHAVIOR_1[1][1] * MIX,
    BEHAVIOR_0[1][2] * (1 - MIX) + BEHAVIOR_1[1][2] * MIX
]

OUTPUT = [LOCATION, ROTATION]    
                """
        self.outputs[0].code = code
        
        self.linked_update()