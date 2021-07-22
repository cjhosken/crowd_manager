from .node_tree import classes as tree_classes
from .point.point_node import CM_PointNode
from .point.point_grid_scatter_node import CM_PointGridScatterNode
from .point.point_join_node import CM_PointJoinNode
from .point.point_transform_node import CM_PointTransformNode
from .point.point_randomize_node import CM_PointRandomizeNode
from .point.point_viewer import CM_PointViewerNode

from .object.object_input_node import CM_ObjectInputNode

from .behavior.jitter_behavior_node import CM_JitterBehaviorNode
from .behavior.constant_behavior_node import CM_ConstantBehaviorNode
from .behavior.script_behavior_node import CM_ScriptBehaviorNode, CM_RefreshNode
from .behavior.merge_behavior_node import CM_MergeBehaviorNode
from .behavior.script_reader_node import CM_ScriptReaderNode

from .agent.agent_node import CM_AgentNode
from .agent.agent_viewer_node import CM_AgentViewerNode

from .crowd.crowd_node import CM_CrowdNode


node_classes = []
node_classes += tree_classes

node_classes += [
    CM_PointNode,
    CM_PointGridScatterNode,
    CM_PointJoinNode,
    CM_PointTransformNode,
    CM_PointRandomizeNode,
    CM_PointViewerNode,

    CM_ObjectInputNode,

    CM_RefreshNode,
    

    CM_JitterBehaviorNode,
    CM_ConstantBehaviorNode,

    CM_ScriptBehaviorNode,
    CM_MergeBehaviorNode,
    CM_ScriptReaderNode,

    CM_AgentNode,
    CM_AgentViewerNode,

    CM_CrowdNode,
]