import bpy
from ..base_node import CrowdManager_BaseNode

class CrowdManager_CombineBehaviorNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_CombineBehaviorNode'
    bl_label = 'Combine Behavior'
    bl_width_default = 150
    bl_icon = 'ERROR'

    node_types = ["behavior"]

    def init(self, context):
        super().__init__()
        #self.inputs.new("CrowdManager_BehaviorSocketType", "Behavior")
        #self.inputs.new("CrowdManager_BehaviorSocketType", "Behavior")
        #self.outputs.new("CrowdManager_BehaviorSocketType", "Behavior")

    def draw_buttons(self, context, layout):
        layout.label(text="This node is broken.")
    
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

LOCATION = [
    BEHAVIOR_0[0][0] + BEHAVIOR_1[0][0] - LAST_SIM.location.x,
    BEHAVIOR_0[0][1] + BEHAVIOR_1[0][1] - LAST_SIM.location.y,
    BEHAVIOR_0[0][2] + BEHAVIOR_1[0][2] - LAST_SIM.location.z
]

ROTATION = [
    BEHAVIOR_0[1][0] + BEHAVIOR_1[1][0] - LAST_SIM.rotation.x,
    BEHAVIOR_0[1][1] + BEHAVIOR_1[1][1] - LAST_SIM.rotation.y,
    BEHAVIOR_0[1][2] + BEHAVIOR_1[1][2] - LAST_SIM.rotation.z
]

OUTPUT = [LOCATION, ROTATION]    
                """
        self.outputs[0].code = code
        
        self.linked_update()