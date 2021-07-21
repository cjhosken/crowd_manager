import bpy
from bpy.props import *
from ..base_node import CM_BaseNode
from ...sockets.point_socket import CM_PointProperty

class CM_PointJoinNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_PointJoinNode'
    bl_label = 'Join Points'

    node_type = ["point"]

    def init(self, context):
        super().__init__()
        self.inputs.new('CM_PointSocketType', "Points")
        self.inputs.new('CM_PointSocketType', "Points")
        self.outputs.new('CM_PointSocketType', "Points")

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