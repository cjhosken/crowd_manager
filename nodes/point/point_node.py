import bpy
from bpy.props import *
from ..base_node import CM_BaseNode
class CM_PointNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_PointNode'
    bl_label = 'Point'
    bl_width_default = 350

    point_location : bpy.props.FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0), update=CM_BaseNode.property_changed)

    node_type = ["point"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CM_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        layout.prop(self, "point_location")
    
    def edit(self):
        pnts = self.outputs[0].points
        if len(pnts) < 1:
            p = pnts.add()
            p.id = 0
            p.location = self.point_location
        else:
            pnts[0].location = self.point_location
        
        self.linked_update()
        