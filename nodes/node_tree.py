from bpy.types import NodeTree, Panel
from nodeitems_utils import NodeCategory, NodeItem

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
    bl_idname = "CROWDMANAGER_PT_SettingsPanel"
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
        NodeItem("CrowdManager_PointNode"),
        NodeItem("CrowdManager_PointGridScatterNode"),
        NodeItem("CrowdManager_PointJoinNode"),
        NodeItem("CrowdManager_PointTransformNode"),
        NodeItem("CrowdManager_PointRandomizeNode"),
        NodeItem("CrowdManager_PointViewerNode"),
    ]),

    CrowdNodeCategory("OBJECT", "Object", items=[
        NodeItem("CrowdManager_ObjectInputNode"),
        NodeItem("CrowdManager_CollectionInputNode"),
    ]),

    CrowdNodeCategory("BEHAVIOR", "Behavior", items=[
        NodeItem("CrowdManager_StaticBehaviorNode"),
        NodeItem("CrowdManager_JitterBehaviorNode"),
        NodeItem("CrowdManager_ScriptBehaviorNode"),
        NodeItem("CrowdManager_MergeBehaviorNode"),
        NodeItem("CrowdManager_CombineBehaviorNode"),
        NodeItem("CrowdManager_BehaviorReaderNode"),
    ]),

    CrowdNodeCategory("AGENT", "Agent", items=[
        NodeItem("CrowdManager_AgentNode"),
        NodeItem("CrowdManager_AgentViewerNode")
    ]),

    CrowdNodeCategory("CROWD", "Crowd", items=[
        NodeItem("CrowdManager_CrowdNode")
    ])

]

classes = [
    CrowdNodeTree,
    CrowdManager_NodeSettingsPanel
]