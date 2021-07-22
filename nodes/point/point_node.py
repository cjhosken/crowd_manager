import bpy
from ..base_node import CrowdManager_BaseNode
class CrowdManager_PointNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_PointNode'
    bl_label = 'Point'
    bl_width_default = 300

    point_location : bpy.props.FloatVectorProperty(name="Location", subtype="TRANSLATION", default=(0, 0, 0), update=CrowdManager_BaseNode.property_changed)
    point_rotation : bpy.props.FloatVectorProperty(name="Rotation", subtype="EULER", default=(0, 0, 0), update=CrowdManager_BaseNode.property_changed)

    node_types = ["point"]

    def init(self, context):
        super().__init__()
        self.outputs.new("CrowdManager_PointSocketType", "Points")

    def draw_buttons(self, context, layout):
        layout.prop(self, "point_location")
        layout.prop(self, "point_rotation")
    
    def edit(self):
        points = self.outputs[0].points
        if len(points) < 1:
            point = points.add()
            point.location = self.point_location
            point.rotation = self.point_rotation
        else:
            points[0].location = self.point_location
            points[0].rotation = self.point_rotation
        
        self.linked_update()
    
    def free(self):
        self.outputs[0].points.clear()
        self.linked_update()
    
    def insert_link(self, link):
        self.edit()
        self.linked_update()