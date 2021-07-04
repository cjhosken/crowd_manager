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

nodeCategories = [
    CrowdNodeCategory("OBJECT", "Object", items=[
        NodeItem("CrowdManager_ObjectInputNode"),
        NodeItem("CrowdManager_CollectionInputNode"),
        NodeItem("CrowdManager_CollectionToObjectNode"),
        NodeItem("CrowdManager_ObjectToCollectionNode")
    ]),
    CrowdNodeCategory("AGENT", "Agent", items=[
        NodeItem("CrowdManager_AgentNode")
    ]),
    CrowdNodeCategory("CROWD", "Crowd", items=[
        NodeItem("CrowdManager_PopulateAgentsNode"),
        NodeItem("CrowdManager_CrowdOutputNode"),
    ]),
    CrowdNodeCategory("BEHAVE", "Behavior", items=[
        NodeItem("CrowdManager_WanderBehaviorNode")
    ]),
    CrowdNodeCategory("POINT", "Point", items=[
        NodeItem("CrowdManager_PointNode"),
        NodeItem("CrowdManager_PointScatterNode"),
        NodeItem("CrowdManager_PointJoinNode"),
        NodeItem("CrowdManager_PointViewerNode"),
    ]),
]

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

classes = [
    CrowdNodeTree,
    CrowdManager_NodeSettingsPanel
]