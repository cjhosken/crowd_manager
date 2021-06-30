import bpy
import addon_utils
from bpy.types import Panel
from bl_ui.utils import PresetPanel

class CrowdManager_PT_Panel(Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

class CrowdManager_PT_BasePanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Crowd Manager"
    bl_idname = "PANEL_PT_crowdmanager"

    def draw(self, context):
        pass

class CrowdManager_PT_GeneralPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Agents"
    bl_idname = "PANEL_PT_crowdmanager_general"
    bl_parent_id = "PANEL_PT_crowdmanager"

    def draw(self, context):
        props = context.window_manager.crowdmanager_props
        layout = self.layout
        row = layout.row()

        row.prop(props, "agent_count", text="Agent Count")
        #row.prop(props, "agent_speed", text="Agent Speed")
        #row.prop(props, "agent_acceleration", text="Agent Acceleration")
        #row.prop(props, "agent_angular_speed", text="Agent Angular Speed")
        #row.prop(props, "agent_angular_acceleration", text="Agent Angular Acceleration")
        #row.prop(props, "agent_space", text="Agent Space")

        row = layout.row()
        row.operator("crowdmanager.simulate", text="Simulate Agents")

class CrowdManager_PT_AgentPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Agents"
    bl_idname = "PANEL_PT_crowdmanager_agents"
    bl_parent_id = "PANEL_PT_crowdmanager"

    def draw(self, context):
        props = context.window_manager.crowdmanager_props
        layout = self.layout
        row = layout.row()

        #row.props(props, "agent_collection", text="Agent Collection")
        #row.operator("crowdmanager.populate", text="Assign Agents")
        pass

class CrowdManager_PT_BehaviorPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Behavior"
    bl_idname = "PANEL_PT_crowdmanager_collide"
    bl_parent_id = "PANEL_PT_crowdmanager_agent"

    def draw(self, context):
        props = context.window_manager.crowdmanager_props
        
        # 2 Controls
        # - Collision Detection
        # - Targets



        #row.props(props, "agent_collision_collection", text="Collision Collection")
        #row.props(props, "self_collisions", text="Agent Collisions")

        #row.prop(props, "collision_sight", text="Collision Sight")
        # allows agents to "see" in front of them, lower values will result in sharper turns to avoid collisions.