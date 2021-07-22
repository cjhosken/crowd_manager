import bpy
from bpy.props import IntVectorProperty, FloatProperty, IntProperty
from ..base_node import CrowdManager_BaseNode

class CrowdManager_PointGridScatterNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_PointGridScatterNode'
    bl_label = 'Point Grid Scatter'
    bl_width_default = 150

    node_types = ["point"]

    grid_size : IntVectorProperty(
        name="Point Grid Size",
        subtype='XYZ',
        size=3,
        default=(10, 10, 1),
        soft_min=1,
        min=1,
        update=CrowdManager_BaseNode.property_changed
    )

    grid_point_spacing : FloatProperty(
        name="Point Spacing",
        default=1,
        soft_min=0.1,
        min=0.1,
        update=CrowdManager_BaseNode.property_changed
    )

    num_sample_before_rejection : IntProperty(
        name="Max Iterations",
        default=5,
        soft_min=1,
        min=1,
        update=CrowdManager_BaseNode.property_changed
    )

    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "grid_point_spacing", text="Grid Spacing ")
        col.prop(self, "grid_size")

    def edit(self):
        points = self.generateGridPoints()
        
        pnts = self.outputs[0].points
        pnts.clear()
        for p in points:
            x = pnts.add()
            x.location = p

        self.linked_update()
    
    def generateGridPoints(self):
        points = []
        w = self.grid_size[0]
        l = self.grid_size[1]
        h = self.grid_size[2]

        gs = self.grid_point_spacing 

        for x in range(w):
            for y in range(l):
                for z in range(h):
                    points.append((x*gs, y*gs, z*gs))
        return points

    def free(self):
        self.outputs[0].points.clear()
        self.linked_update()