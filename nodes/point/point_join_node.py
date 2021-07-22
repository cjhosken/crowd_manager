import bpy
from ..base_node import CrowdManager_BaseNode

class CrowdManager_PointJoinNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_PointJoinNode'
    bl_label = 'Join Points'

    node_types = ["point"]

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        pnts = self.outputs[0].points
        node0 = self.get_input_node(0)
        node1 = self.get_input_node(1)

        pnts.clear()

        if node0 is None: 
            if node1 is not None:
                for p in node1.outputs[0].points:
                    x = pnts.add()
                    x.location = p.location
        else:
            if node1 is None:
                for p in node0.outputs[0].points:
                    x = pnts.add()
                    x.location = p.location
            else:
                for p in node0.outputs[0].points:
                    x = pnts.add()
                    x.location = p.location

                for p in node1.outputs[0].points:
                    x = pnts.add()
                    x.location = p.location