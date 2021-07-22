from bpy.types import *
from bpy_types import *
from nodeitems_utils import *

class CrowdNodeTree(NodeTree):
    '''CrowdManager node editor'''
    bl_idname = "crowdmanager_node_tree"
    bl_label = "CrowdManager"
    bl_icon = "COMMUNITY"

    def update(self):
        pass

class CrowdNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'crowdmanager_node_tree'

class CrowdManager_NodeSettingsPanel(Panel):
    bl_idname = "CROWDMANAGER_PT_settings_panel"
    bl_label = "CrowdManager"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "CrowdManager"

    @classmethod
    def poll(cls, context):
        pass

    def draw(self, context):
        pass

node_categories = [
    CrowdNodeCategory("POINT", "Point", items=[
        NodeItem("CM_PointNode"),
        NodeItem("CM_PointGridScatterNode"),
        NodeItem("CM_PointJoinNode"),
        NodeItem("CM_PointTransformNode"),
        NodeItem("CM_PointRandomizeNode"),
        NodeItem("CM_PointViewerNode"),
    ]),

    CrowdNodeCategory("OBJECT", "Object", items=[
        NodeItem("CM_ObjectInputNode"),
    ]),

    CrowdNodeCategory("BEHAVIOR", "Behavior", items=[
        NodeItem("CM_JitterBehaviorNode"),
        NodeItem("CM_ConstantBehaviorNode"),
        NodeItem("CM_ScriptBehaviorNode"),
        NodeItem("CM_MergeBehaviorNode"),
        NodeItem("CM_ScriptReaderNode"),
    ]),

    CrowdNodeCategory("AGENT", "Agent", items=[
        NodeItem("CM_AgentNode"),
        NodeItem("CM_AgentViewerNode")
    ]),

    CrowdNodeCategory("CROWD", "Crowd", items=[
        NodeItem("CM_CrowdNode")
    ])

]

classes = [
    CrowdNodeTree,
    CrowdManager_NodeSettingsPanel
]