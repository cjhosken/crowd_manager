from math import pi
from bgl import GL_POINT
import bpy
from bpy.props import *
from ..base_node import CM_BaseNode
import random
from ...sockets.point_socket import CM_PointProperty

class CM_PointRandomizeNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_PointRandomizeNode'
    bl_label = 'Point Randomize'
    bl_width_default = 150

    node_type = ["point"]

    seed : IntProperty(name="Seed", default=0, min=0, update=CM_BaseNode.property_changed)

    min_translate : FloatVectorProperty(name="Min Translate", subtype="TRANSLATION", default=(-1, -1, -1), update=CM_BaseNode.property_changed)
    max_translate : FloatVectorProperty(name="Max Translate", subtype="TRANSLATION", default=(1, 1, 1), update=CM_BaseNode.property_changed)

    min_rotate : FloatVectorProperty(name="Min Rotate", subtype="EULER", default=(-pi, -pi, -pi), update=CM_BaseNode.property_changed)
    max_rotate : FloatVectorProperty(name="Max Rotate", subtype="EULER", default=(pi, pi, pi), update=CM_BaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new("CM_PointSocketType", "Points")
        self.outputs.new("CM_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "seed")
        col.prop(self, "min_translate")
        col.prop(self, "max_translate")
        col = layout.column()
        col.prop(self, "min_rotate")
        col.prop(self, "max_rotate")

    def edit(self):
        pnts = self.outputs[0].points
        node = self.get_input_node(idx=0)

        pnts.clear()

        if node is not None:
            random.seed(self.seed)
            for p in node.outputs[0].points:
                x = pnts.add()
                x.location = (
                    p.location.x + random.uniform(self.min_translate.x, self.max_translate.x), 
                    p.location.y + random.uniform(self.min_translate.y, self.max_translate.y), 
                    p.location.z +  random.uniform(self.min_translate.z, self.max_translate.z)
                )
