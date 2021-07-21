from .node_tree import classes as tree_classes
from .point.point_node import CM_PointNode
from .point.point_grid_scatter_node import CM_PointGridScatterNode
from .point.point_join_node import CM_PointJoinNode
from .point.point_transform_node import CM_PointTransformNode
from .point.point_randomize_node import CM_PointRandomizeNode
from .point.point_viewer import CM_PointViewerNode

from .behavior.script_behavior_node import CM_ScriptBehaviorNode

from .agent.agent_node import CM_AgentNode
from .agent.agent_viewer_node import CM_AgentViewerNode


node_classes = []
node_classes += tree_classes

node_classes += [
    CM_PointNode,
    CM_PointGridScatterNode,
    CM_PointJoinNode,
    CM_PointTransformNode,
    CM_PointRandomizeNode,
    CM_PointViewerNode,

    CM_ScriptBehaviorNode,

    CM_AgentNode,
    CM_AgentViewerNode,
]