from .node_tree import classes as node_tree_classes
from .point.point_node import CrowdManager_PointNode
from .point.point_scatter_node import CrowdManager_PointScatterNode
from .point.point_viewer_node import CrowdManager_PointViewerNode
from .point.point_join_node import CrowdManager_PointJoinNode

from .object.object_input_node import CrowdManager_ObjectInputNode
from .object.collection_input_node import CrowdManager_CollectionInputNode
from .object.object_to_collection_node import CrowdManager_ObjectToCollectionNode
from .object.collection_to_object_node import CrowdManager_CollectionToObjectNode

from .behavior.jitter_behavior_node import CrowdManager_JitterBehaviorNode

from .agent.agent_node import CrowdManager_AgentNode
from .agent.agent_viewer_node import CrowdManager_AgentViewerNode

from .crowd.crowd_node import CrowdManager_CrowdNode

node_classes = node_tree_classes + [
        CrowdManager_PointNode,
        CrowdManager_PointScatterNode,
        CrowdManager_PointViewerNode,
        CrowdManager_PointJoinNode,

        CrowdManager_ObjectInputNode,
        CrowdManager_CollectionInputNode,
        CrowdManager_ObjectToCollectionNode,
        CrowdManager_CollectionToObjectNode,

        CrowdManager_JitterBehaviorNode,

        CrowdManager_AgentNode,
        CrowdManager_AgentViewerNode,

        CrowdManager_CrowdNode
    ]