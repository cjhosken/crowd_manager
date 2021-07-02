from bpy.types import Collection, PropertyGroup, UIList
from bpy.props import BoolProperty, CollectionProperty, EnumProperty, IntProperty, FloatProperty, PointerProperty, StringProperty
import __init__
import bpy
import modules.agent as agent

parent_path = __init__.parent_path
class CrowdManager_Properties(PropertyGroup):
    agents = []

    agent_count : IntProperty(
        name="Agent count",
        description="Number of agents used for simulating",
        min=0,
        default = 10,
    )

    agent_velocity : FloatProperty(
        name="Agent velocity",
        description="Max velocity of agents",
        min=0,
        default=1.0,
    )

    agent_acceleration : FloatProperty(
        name="Agent acceleration",
        description="Max amount of acceleration achieved by agents",
        min=0,
        default = 0.25,
    )

    agent_angular_velocity : FloatProperty(
        name="Agent angular velocity",
        description="Max angular velocity of agents",
        min=0,
        default=1.0,
    )

    agent_angular_acceleration : FloatProperty(
        name="Agent angular acceleration",
        description="Max amount of angular acceleration achieved by agents",
        min=0,
        default = 0.25,
    )

    agent_space : FloatProperty(
        name="Agent space",
        description="Smallest amount of space between 2 agents",
        min=0,
        default = 1,
    )

    agent_collection : PointerProperty(
        type= bpy.types.Collection,
        name="Agent Collection",
        description="Collection used to populate agents",
    )

    collision_collection : PointerProperty(
        type= bpy.types.Collection,
        name="Collision Collection",
        description="Collection used for agent collisions",
    )

    self_collision : BoolProperty(
        name="Self Collisions",
        description="Toggle agent self collisions",
        default=True,
    )

    collision_sight : FloatProperty(
        name="Collision Sight",
        description="Distance threshold in which agents can detect an incoming collision",
        min=0,
        default = 2.0,
    )

    seed : IntProperty(
        name="Seed",
        description= "seed for agent simulation",
        min=0,
        default = 1
    )

    scatter_surface : PointerProperty(
        type= bpy.types.Object,
        name="Surface",
        description="Object used to scatter agents",
    )

    use_vertex_group : BoolProperty(
        name="Use Vertex Group",
        description= "Use surface object vertex group, 'crowd'",
        default = False,
    )