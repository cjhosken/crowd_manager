import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

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

        out_points = {"points" : []}
        
        if node0 is None: 
            if node1 is not None:
                out_points = node1.outputs[0].points
        else:
            if node1 is None:
                out_points = node0.outputs[0].points
            else:
                points0 = json.loads(node0.outputs[0].points)
                points1 = json.loads(node1.outputs[0].points)
                for p0 in points0["points"]:
                    out_points["points"].append(p0)
                for p1 in points1["points"]:
                    out_points["points"].append(p1)
        
        if len(self.outputs) > 0:
            self.outputs[0].points = json.dumps(out_points)
        self.link_update()
        

        
