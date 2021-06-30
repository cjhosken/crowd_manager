from bpy.types import PropertyGroup
from bpy.props import BoolProperty, EnumProperty, IntProperty, FloatProperty
import __init__

parent_path = __init__.parent_path

class CrowdManager_Properties(PropertyGroup):
    agent_count : IntProperty(
        name="Agent Count",
        description="Numer of agents used for simulating.",
        default = 10,
    )