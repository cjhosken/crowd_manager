import bpy
from bpy.props import *
from ..base_node import CrowdManagerBaseNode

import json
import math
from random import uniform, random, randrange
from mathutils import Vector
from ...types.point import CM_PointList, CM_Point

class CrowdManager_PointScatterNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PointScatterNode'
    bl_label = 'Point Scatter'

    node_type = "point"

    scatter_type : EnumProperty(
        name = "Scatter Type",
        description="",
        items = [
            ('GRID', "Grid Scatter", ""),
            ('POISSON', "Poisson Scatter", "")
        ],
        default='GRID',
        update=CrowdManagerBaseNode.property_changed
    )

    radius : FloatProperty(
        name="Point Radius",
        default=2.0,
        soft_min=0.1,
        min=0.1,
        update=CrowdManagerBaseNode.property_changed
    )

    sample_region_size : FloatVectorProperty(
        name="Region Size",
        subtype='XYZ',
        size=3,
        default=(10.0, 10.0, 0.0),
        soft_min=1.0,
        min=1,
        update=CrowdManagerBaseNode.property_changed
    )

    grid_size : IntVectorProperty(
        name="Point Grid Size",
        subtype='XYZ',
        size=3,
        default=(10, 10, 1),
        soft_min=1,
        min=1,
        update=CrowdManagerBaseNode.property_changed
    )

    grid_point_spacing : FloatProperty(
        name="Point Spacing",
        default=1,
        soft_min=0.1,
        min=0.1,
        update=CrowdManagerBaseNode.property_changed
    )

    num_sample_before_rejection : IntProperty(
        name="Max Iterations",
        default=5,
        soft_min=1,
        min=1,
        update=CrowdManagerBaseNode.property_changed
    )

    points : bpy.props.StringProperty(name="Points", default=CM_PointList().toJSON())


    def init(self, context):
        super().__init__()
        self.outputs.new('CrowdManager_PointSocketType', "Points")

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "scatter_type")
        if self.scatter_type == "GRID":
            self.draw_grid(context, layout)
        elif self.scatter_type == "POISSON":
            self.draw_poisson(context, layout)

    def edit(self):
        self.points = CM_PointList().toJSON()
        points = CM_PointList(dict=CM_PointList.fromJSON(self.points))
        if self.scatter_type == "POISSON":
            points = self.generatePoissonPoints(points)
        elif self.scatter_type == "GRID":
            points = self.generateGridPoints(points)

        self.outputs[0].points = points.toJSON()
        self.link_update()
        

# Grid Scattering
#################################################
    def draw_grid(self, context, layout):
        col = layout.column()
        col.prop(self, "grid_point_spacing")
        col.prop(self, "grid_size")
    
    def generateGridPoints(self, points):
        w = self.grid_size[0]
        l = self.grid_size[1]
        h = self.grid_size[2]

        gs = self.grid_point_spacing 

        for x in range(w):
            for y in range(l):
                for z in range(h):
                    pnt = CM_Point([x*gs, y*gs, z*gs], [0.0, 0.0, 0.0])
                    points.add(pnt)
        return points

# Poisson Disk Scattering
#################################################
    def draw_poisson(self, context, layout):
        col = layout.column()
        col.prop(self, "radius")
        col.prop(self, "sample_region_size")
        col.prop(self, "num_sample_before_rejection")


    def generatePoissonPoints(self, points):
        cell_size = self.radius / math.sqrt(2)
        grid = [[0 for j in range(math.ceil(self.sample_region_size.y / cell_size))] for i in range(math.ceil(self.sample_region_size.x / cell_size))]
        spawn_points = []
        spawn_points.append(self.sample_region_size / 2)

        while len(spawn_points) > 0:
            spawn_index = randrange(len(spawn_points))
            spawn_center = spawn_points[spawn_index]
            cand_accepted = False

            for i in range(self.num_sample_before_rejection):
                angle = random() * math.pi * 2
                direction = Vector((math.sin(angle), math.cos(angle), 0))
                candidate = spawn_center + direction * uniform(self.radius, 2 * self.radius)
                if self.isValid(candidate, cell_size, points, grid):
                    points.add(CM_Point([candidate.x, candidate.y, 0], [0, 0, 0]))
                    spawn_points.append(candidate)
                    grid[int(candidate.x / cell_size)][int(candidate.y / cell_size)] = len(points.points)
                    cand_accepted = True
                    break

            if not cand_accepted:
                spawn_points.pop(spawn_index)
        
        return points

    def isValid(self, candidate, cell_size, points, grid):
        if candidate.x >= 0 and candidate.x < self.sample_region_size.x and candidate.y >= 0 and candidate.y < self.sample_region_size.y:
            cell = candidate / cell_size
            search_start = Vector((max(0, int(cell.x) - 2), max(0, int(cell.y) - 2), 0))
            search_end = Vector((min(int(cell.x) + 2, len(grid) - 1), min(int(cell.y) + 2, len(grid[0]) - 1), 0))

            for x in range(int(search_start.x), int(search_end.x + 1)):
                for y in range(int(search_start.y), int(search_end.y + 1)):
                    point_index = grid[x][y] - 1

                    if point_index != -1:
                        cand = Vector((candidate.x, candidate.y, 0))
                        point = Vector((points.points[point_index].location[0], points.points[point_index].location[1], 0))
                        dist_vec = cand - point
                        dist = math.sqrt(dist_vec.x**2 + dist_vec.y**2 + dist_vec.z**2)
                        if dist < self.radius:
                            return False
            return True
        return False
