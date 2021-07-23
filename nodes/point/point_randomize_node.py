import bpy
import random
from math import pi as PI
from bpy.props import EnumProperty, IntProperty, FloatProperty, FloatVectorProperty
from ..base_node import CrowdManager_BaseNode

class CrowdManager_PointRandomizeNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_PointRandomizeNode'
    bl_label = 'Point Randomize'
    bl_width_default = 150

    node_types = ["point"]

    settings : EnumProperty(name="Type", items=[
        ("simp", "Simple", ""),
        ("adv", "Advanced", ""),
    ])

    seed : IntProperty(name="Seed", default=0, min=0, update=CrowdManager_BaseNode.property_changed)

    min_translate : FloatVectorProperty(name="Min Translate", subtype="TRANSLATION", default=(-1, -1, -1), update=CrowdManager_BaseNode.property_changed)
    max_translate : FloatVectorProperty(name="Max Translate", subtype="TRANSLATION", default=(1, 1, 1), update=CrowdManager_BaseNode.property_changed)

    min_rotate : FloatVectorProperty(name="Min Rotate", subtype="EULER", default=(-PI, -PI, -PI), update=CrowdManager_BaseNode.property_changed)
    max_rotate : FloatVectorProperty(name="Max Rotate", subtype="EULER", default=(PI, PI, PI), update=CrowdManager_BaseNode.property_changed)

    simple_translate : FloatProperty(name="Translate", default=1, update=CrowdManager_BaseNode.property_changed)
    simple_rotate : FloatProperty(name="Rotate", default=1, update=CrowdManager_BaseNode.property_changed)

    def init(self, context):
        super().__init__()
        self.inputs.new("CrowdManager_PointSocketType", "Points")
        self.outputs.new("CrowdManager_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "settings")
        col.prop(self, "seed", text="Seed:")

        if self.settings == "adv":
            col.label(text="Translate:")
            col.prop(self, "min_translate", text="Min")
            col.prop(self, "max_translate", text="Max")
            col.label(text="Rotate:")
            col.prop(self, "min_rotate", text="Min")
            col.prop(self, "max_rotate", text="Max")
        
        elif self.settings == "simp":
            col.prop(self, "simple_translate", text="Location:")
            col.prop(self, "simple_rotate", text="Rotation: ")

    def edit(self):
        points = self.outputs[0].points
        node = self.get_input_node(idx=0)

        points.clear()

        if node is not None:
            random.seed(self.seed)

            for in_point in node.outputs[0].points:
                out_point = points.add()
                if self.settings == "adv":
                    out_point.location = (
                        in_point.location.x + random.uniform(self.min_translate.x, self.max_translate.x), 
                        in_point.location.y + random.uniform(self.min_translate.y, self.max_translate.y), 
                        in_point.location.z +  random.uniform(self.min_translate.z, self.max_translate.z)
                    )
                    out_point.rotation = (
                        in_point.rotation.x + random.uniform(self.min_rotate.x, self.max_rotate.x), 
                        in_point.rotation.y + random.uniform(self.min_rotate.y, self.max_rotate.y), 
                        in_point.rotation.z +  random.uniform(self.min_rotate.z, self.max_rotate.z)
                    )
                elif self.settings == "simp":
                    out_point.location = (
                        in_point.location.x + random.uniform(-self.simple_translate, self.simple_translate),
                        in_point.location.y + random.uniform(-self.simple_translate, self.simple_translate),
                        in_point.location.z + random.uniform(-self.simple_translate, self.simple_translate)
                    )

                    out_point.rotation = (
                        in_point.rotation.x + random.uniform(-self.simple_rotate, self.simple_rotate),
                        in_point.rotation.y + random.uniform(-self.simple_rotate, self.simple_rotate),
                        in_point.rotation.z + random.uniform(-self.simple_rotate, self.simple_rotate)
                    )
