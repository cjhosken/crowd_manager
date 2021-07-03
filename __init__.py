#
#    Copyright (C) 2021 Christopher Hosken
#    hoskenchristopher@gmail.com
#
#    Created by Christopher Hosken
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

bl_info = {
    "name" : "Crowd Manager",
    "author" : "Christopher Hosken, Gurpeet Singh",
    "description" : "Node based visual scripting designed for creating large crowds in Blender.",
    "blender" : (3, 0, 0),
    "version" : (3, 0, 0),
    "location" : "CrowdManager Editor",
    "warning" : "This version is still in development.",
    "category" : "Node"
}

from . import auto_load
from .nodes import node_classes
from .sockets import socket_classes
from .operators import operator_classes
from .preferences import classes as preference_classes
import nodeitems_utils

classes = []
classes += preference_classes
classes += operator_classes
classes += node_classes
classes += socket_classes

auto_load.init()

def register():
    from bpy.utils import register_class
    from .nodes.node_tree import nodeCategories

    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('CROWDMANAGER_NODES', nodeCategories)

def unregister():
    from bpy.utils import unregister_class
    nodeitems_utils.unregister_node_categories('CROWDMANAGER_NODES')

    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    try:
        register()
    except Exception as e:
        print(e)