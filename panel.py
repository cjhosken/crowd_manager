import bpy
import addon_utils
from bpy.types import Panel
from bl_ui.utils import PresetPanel
import __init__

class CrowdManager_PT_Panel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

class CrowdManager_PT_BasePanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Crowd Manager"
    bl_idname = "PANEL_PT_crowdmanager"

    def draw(self, context):
        pass

class CrowdManager_PT_AgentPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Agents"
    bl_idname = "PANEL_PT_crowdmanager_agents"
    bl_parent_id = "PANEL_PT_crowdmanager"

    def draw(self, context):
        props = context.scene.crowdmanager_props
        layout = self.layout
        layout.use_property_split = True
        
        col = layout.column()

        col.prop(props, "scatter_surface")
        col.prop(props, "agent_collection")

        col.operator("crowdmanager.distribute", text="Scatter Agents", icon="OUTLINER_OB_POINTCLOUD")

        row = col.row()
        row.operator("crowdmanager.simulate", text="Simulate Agents", icon="OUTLINER_OB_ARMATURE")
        row.operator("crowdmanager.desimulate", text="", icon='X')
        
        row = col.row()
        row.operator("crowdmanager.populate", text="Populate Agents", icon="COMMUNITY")
        row.operator("crowdmanager.depopulate", text="", icon='X')

class CrowdManager_PT_GeneralPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "General"
    bl_idname = "PANEL_PT_crowdmanager_general"
    bl_parent_id = "PANEL_PT_crowdmanager"

    def draw(self, context):
        props = context.scene.crowdmanager_props
        layout = self.layout
        layout.use_property_split = True

        col = layout.column()
        col.prop(props, "seed")
        col.prop(props, "agent_count")
        col.prop(props, "agent_velocity")
        col.prop(props, "agent_acceleration")
        col.prop(props, "agent_angular_velocity")
        col.prop(props, "agent_angular_acceleration")
        col.prop(props, "agent_space")

class CrowdManager_PT_BehaviorPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Behaviors"
    bl_idname = "PANEL_PT_crowdmanager_collide"
    bl_parent_id = "PANEL_PT_crowdmanager"

    def draw(self, context):
        props = context.scene.crowdmanager_props
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        row = layout.row()
        row.template_list("CROWDMANAGER_UL_BehaviorItems", "", context.scene, "crowdmanager_behaviors", context.scene, "crowdmanager_index", rows=4)
        col = row.column()
        sub = col.row()
        subsub = sub.column(align=True)
        subsub.operator_menu_enum("crowdmanager.behavior_add", "behavior", icon='ADD', text="")
        subsub.operator("crowdmanager.behavior_actions", icon='REMOVE', text="").action = 'REMOVE'
        sub = col.row()
        subsub = sub.column(align=True)
        subsub.operator("crowdmanager.behavior_actions", icon='TRIA_UP', text="").action = 'UP'
        subsub.operator("crowdmanager.behavior_actions", icon='TRIA_DOWN', text="").action = 'DOWN'

        if len(context.scene.crowdmanager_behaviors) > 0:
            rule = context.scene.crowdmanager_behaviors[context.scene.crowdmanager_index]
            if rule:
                col = layout.column()

                if rule.behavior == "Collisions":
                    col.label(text="Collisions")
                    col.prop(props, "collision_collection")
                    col.prop(props, "collision_sight", text="Collision Sight")
                    col.prop(props, "self_collision", text="Self Collision")

                elif rule.behavior == "Targets":
                    col.label(text="Targets")
                    
                    if len(context.scene.crowdmanager_targets) > 0:
                        box = layout.box()
                        for i, t in enumerate(context.scene.crowdmanager_targets):
                            row = box.row()
                            row.prop(t, "object", text="Target Object" if t.object is None else t.object.name)
                            row.prop(t, "attraction")
                            row.prop(t, "max_distance")
                            row.operator("crowdmanager.del_target", text="", icon='X', emboss=False).index = i

                    col = layout.column()
                    col.operator("crowdmanager.add_target", text="", icon='ADD', emboss=False)

                elif rule.behavior == "Random":
                    col.label(text="Random")
                    # cool extra control method go here.


class CrowdManager_PT_ExtraPanel(CrowdManager_PT_Panel, Panel):
    bl_label = "Extra"
    bl_idname = "PANEL_PT_crowdmanager_extra"
    bl_parent_id = "PANEL_PT_crowdmanager"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        col = layout.column()
        col.label(text="Info:")
        col.operator("wm.url_open", text="Report Bug", icon='URL').url = "https://github.com/Christopher-Hosken/crowdManager/issues"
        col = layout.column()
        col.label(text="Contact:")
        col.operator("wm.url_open", text="Christopher Hosken").url = "https://github.com/Christopher-Hosken"
        col.operator("wm.url_open", text="Gurpeet Singh").url = "https://github.com/gurpreetsingh-exe"
