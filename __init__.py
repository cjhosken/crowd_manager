  
#    This software free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

__copyright__ = "(c) 2021,  Christopher Hosken"
__license__ = "GPL v3"

bl_info = {
    "name": "crowdManager",
    "author": "Christopher Hosken",
    "version": (1, 0, 0),
    "blender": (2, 92, 0),
    "warning": "",
    "category": "Animation"
}

import bpy
import sys
import os
from importlib import reload
parent_path = None

try:
    parent_path = os.path.dirname(__file__)
except:
    pass
try:
    parent_path = os.path.dirname(bpy.context.space_data.text.filepath)
except:
    pass

if (parent_path is None):
    raise FileNotFoundError("Cannot locate path 'parent_path'.")

sys.path.append(parent_path)

module_list = ["simulate", "agent"]

for module_name in module_list:
    if (module_name in sys.modules):
        reload(sys.modules[module_name])

import modules.simulate as simulate
import modules.agent as agent
import panel
import props

classes = [
    props.CrowdManager_Properties,
    simulate.CrowdManager_OT_Simulate,
    panel.CrowdManager_PT_Panel,
    panel.CrowdManager_PT_BasePanel,
    panel.CrowdManager_PT_GeneralPanel,
    panel.CrowdManager_PT_AgentPanel,
    panel.CrowdManager_PT_CollisionsPanel,
]

ag = agent.Agent(1)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.WindowManager.crowdmanager_props = bpy.props.PointerProperty(type=props.CrowdManager_Properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.WindowManager.crowdmanager_props

if __name__ == "__main__":
    try:
        register()
    except ValueError as e:
        print(e)
        unregister()
        register()