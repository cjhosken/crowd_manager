import bpy
from bpy.types import (Operator,
                       UIList)

# -------------------------------------------------------------------
#   Operators
# -------------------------------------------------------------------

class CrowdManager_OT_BehaviorActions(Operator):
    """Move items up and down, add and remove"""
    bl_idname = "crowdmanager.behavior_actions"
    bl_label = "Behavior Actions"
    bl_description = "Move items up and down, add and remove"
    bl_options = {'REGISTER'}

    action: bpy.props.EnumProperty(
        items=(
            ('UP', "Up", ""),
            ('DOWN', "Down", ""),
            ('REMOVE', "Remove", ""),
            ('ADD', "Add", "")))

    def invoke(self, context, event):
        scn = context.scene
        idx = scn.crowdmanager_index

        try:
            item = scn.crowdmanager_behaviors[idx]
        except IndexError:
            pass
        else:
            if self.action == 'DOWN' and idx < len(scn.crowdmanager_behaviors) - 1:
                scn.crowdmanager_behaviors.move(idx, idx+1)
                scn.crowdmanager_index += 1

            elif self.action == 'UP' and idx >= 1:
                scn.crowdmanager_behaviors.move(idx, idx-1)
                scn.crowdmanager_index -= 1
                if scn.crowdmanager_index < 0:
                    scn.crowdmanager_index = 0    

            elif self.action == 'REMOVE':
                scn.crowdmanager_index -= 1    
                if scn.crowdmanager_index < 0:
                    scn.crowdmanager_index = 0        
                scn.crowdmanager_behaviors.remove(idx)

        return {"FINISHED"}

class CrowdManager_OT_AddBehavior(Operator):
    bl_idname = "crowdmanager.behavior_add"
    bl_label = "Add Behavior"
    bl_description = "Test"

    behavior: bpy.props.EnumProperty(
        name="Behavior Type",
        description="behavior types for crowds.",
        items = [
            ('Collisions', 'Collisions', "", "", 0),
            ('Targets', 'Targets', "", "", 1),
            ('Random', 'Random', "", "", 2)
        ]
    )

    def execute(self, context):
        for b in context.scene.crowdmanager_behaviors:
            if b.behavior == self.behavior:
                break
        else:
            b = context.scene.crowdmanager_behaviors.add()
            b.behavior = self.behavior
            b.name = self.behavior

        return {'FINISHED'}


class CROWDMANAGER_UL_BehaviorItems(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=" " + item.behavior)

    def invoke(self, context, event):
        pass  

class CROWDMANAGER_BehaviorCollection(bpy.types.PropertyGroup):
    behavior: bpy.props.EnumProperty(
        name="Behavior Type",
        description="behavior types for crowds.",
        items = [
            ('Collisions', 'Collisions', "", "", 0),
            ('Targets', 'Targets', "", "", 1),
            ('Random', 'Random', "", "", 2)
        ]
    )
