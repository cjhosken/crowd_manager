import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...sockets.utils import point_list_to_string, string_to_point_list

class CrowdManager_PointJoinNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointJoinNode'
    bl_label = 'Join Points'

    node_type = "point"

    #remove_doubles : BoolProperty(default=False, update = CrowdManagerBaseNode.property_changed)
    #merge_distance : FloatProperty(default = 0.001, update = CrowdManagerBaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_PointSocketType', "Points")
        self.inputs.new('CrowdManager_PointSocketType', "Points")

        self.outputs.new('CrowdManager_PointSocketType', "Points")
        
    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)

        if node0 is None:
            if node1 is None:
                out = []
            else:
                out = string_to_point_list(node1.outputs[0].points)
        elif node1 is None:
            out = string_to_point_list(node0.outputs[0].points)
        else:
            pnts0 = string_to_point_list(node0.outputs[0].points)
            pnts1 = string_to_point_list(node1.outputs[0].points)
            out = pnts0 + pnts1

        
        if len(self.outputs) > 0:
            self.outputs[0].points = point_list_to_string(out)

        self.link_update()
        

        
