from .node_tree import classes as tree_classes
from .point.point_node import CrowdManager_PointNode
from .point.point_grid_scatter_node import CrowdManager_PointGridScatterNode
from .point.point_join_node import CrowdManager_PointJoinNode
from .point.point_transform_node import CrowdManager_PointTransformNode
from .point.point_randomize_node import CrowdManager_PointRandomizeNode
from .point.point_viewer import CrowdManager_PointViewerNode

from .object.object_input_node import CrowdManager_ObjectInputNode
from .object.collection_input_node import CrowdManager_CollectionInputNode

from .behavior.static_behavior_node import CrowdManager_StaticBehaviorNode
from .behavior.jitter_behavior_node import CrowdManager_JitterBehaviorNode
from .behavior.script_behavior_node import CrowdManager_ScriptBehaviorNode, CrowdManager_OT_NodeRefresh
from .behavior.merge_behavior_node import CrowdManager_MergeBehaviorNode
from .behavior.combine_behavior_node import CrowdManager_CombineBehaviorNode
from .behavior.behavior_reader_node import CrowdManager_BehaviorReaderNode, CrowdManager_OT_SaveBehavior

from .agent.agent_node import CrowdManager_AgentNode
from .agent.agent_viewer_node import CrowdManager_AgentViewerNode

from .crowd.crowd_node import CrowdManager_CrowdNode


node_classes = []
node_classes += tree_classes

node_classes += [
    CrowdManager_PointNode,
    CrowdManager_PointGridScatterNode,
    CrowdManager_PointJoinNode,
    CrowdManager_PointTransformNode,
    CrowdManager_PointRandomizeNode,
    CrowdManager_PointViewerNode,

    CrowdManager_ObjectInputNode,
    CrowdManager_CollectionInputNode,

    CrowdManager_OT_NodeRefresh,
    
    CrowdManager_JitterBehaviorNode,
    CrowdManager_CombineBehaviorNode,
    CrowdManager_StaticBehaviorNode,
    CrowdManager_ScriptBehaviorNode,
    CrowdManager_MergeBehaviorNode,
    CrowdManager_BehaviorReaderNode,
    CrowdManager_OT_SaveBehavior,

    CrowdManager_AgentNode,
    CrowdManager_AgentViewerNode,

    CrowdManager_CrowdNode,
]