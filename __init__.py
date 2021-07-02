  
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

__copyright__ = "(c) 2021, Christopher Hosken"
__license__ = "GPL v3"

bl_info = {
    "name": "crowdManager",
    "author": "Christopher Hosken, Gurpeet Singh",
    "version": (1, 0, 0),
    "blender": (2, 92, 0),
    "warning": "",
    "category": "Animation"
}

import bpy
import sys
import os
from importlib import reload

from bpy.props import IntProperty
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

module_list = ["simulate", "agent", "addon_props", "panel", "populate", "distribute", "behaviors", "targets"]

for module_name in module_list:
    if (module_name in sys.modules):
        reload(sys.modules[module_name])

import modules.simulate as simulate
import modules.populate as populate
import modules.behaviors as behaviors
import modules.distribute as distribute
import modules.targets as targets
import modules.agent as agent
import panel
import addon_props

classes = [
    addon_props.CrowdManager_Properties,
    targets.CROWDMANAGER_TargetCollection,
    targets.CrowdManager_OT_DeleteTarget,
    targets.CrowdManager_OT_AddTarget,
    behaviors.CROWDMANAGER_UL_BehaviorItems,
    behaviors.CrowdManager_OT_BehaviorActions,
    behaviors.CrowdManager_OT_AddBehavior,
    behaviors.CROWDMANAGER_BehaviorCollection,
    distribute.CrowdManager_OT_Distribute,
    simulate.CrowdManager_OT_Simulate,
    simulate.CrowdManager_OT_ClearSimulations,
    populate.CrowdManager_OT_Populate,
    populate.CrowdManager_OT_DePopulate,
    panel.CrowdManager_PT_BasePanel,
    panel.CrowdManager_PT_AgentPanel,
    panel.CrowdManager_PT_GeneralPanel,
    panel.CrowdManager_PT_BehaviorPanel,
    panel.CrowdManager_PT_ExtraPanel,
]

def register():    
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.crowdmanager_props = bpy.props.PointerProperty(type=addon_props.CrowdManager_Properties)
    bpy.types.Scene.crowdmanager_behaviors = bpy.props.CollectionProperty(type=behaviors.CROWDMANAGER_BehaviorCollection)
    bpy.types.Scene.crowdmanager_targets = bpy.props.CollectionProperty(type=targets.CROWDMANAGER_TargetCollection)
    bpy.types.Scene.crowdmanager_index = IntProperty()
    agent.Agent.ReloadAgents()

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.crowdmanager_props
    del bpy.types.Scene.crowdmanager_behaviors
    del bpy.types.Scene.crowdmanager_index
    del bpy.types.Scene.crowdmanager_targets

if __name__ == "__main__":
    try:
        register()
    except Exception as e:
        print(e)