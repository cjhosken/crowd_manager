from .node_tree import classes as node_tree_classes
from .point.point_node import CrowdManager_PointNode
from .point.point_scatter_node import CrowdManager_PointScatterNode
from .point.point_viewer_node import CrowdManager_PointViewerNode
from .point.point_join_node import CrowdManager_PointJoinNode

from .behavior.jitter_behavior_node import CrowdManager_JitterBehaviorNode

from .agent.agent_node import CrowdManager_AgentNode
from .agent.agent_viewer_node import CrowdManager_AgentViewerNode

node_classes = node_tree_classes + [
        CrowdManager_PointNode,
        CrowdManager_PointScatterNode,
        CrowdManager_PointViewerNode,
        CrowdManager_PointJoinNode,

        CrowdManager_JitterBehaviorNode,

        CrowdManager_AgentNode,
        CrowdManager_AgentViewerNode
    ]