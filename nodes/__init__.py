from .node_tree import classes as node_tree_classes
from .object.object_input_node import CrowdManager_ObjectInputNode
from .object.collection_input_node import CrowdManager_CollectionInputNode
from .object.collection_to_object_node import CrowdManager_CollectionToObjectNode
from .object.object_to_collection_node import CrowdManager_ObjectToCollectionNode

from .agents.agent_node import CrowdManager_AgentNode

from .crowd.populate_agents_node import CrowdManager_PopulateAgentsNode
from .crowd.crowd_output_node import CrowdManager_CrowdOutputNode

from .behavior.wander_behavior_node import CrowdManager_WanderBehaviorNode

from .point.object_point_scatter_node import CrowdManager_ObjectPointScatterNode
from .point.point_node import CrowdManager_PointNode
from .point.point_viewer import CrowdManager_PointViewer
from .point.point_join import CrowdManager_PointJoin

node_classes = node_tree_classes + [
        CrowdManager_ObjectInputNode,
        CrowdManager_CollectionInputNode,
        CrowdManager_CollectionToObjectNode,
        CrowdManager_ObjectToCollectionNode,

        CrowdManager_AgentNode,

        CrowdManager_PopulateAgentsNode,
        CrowdManager_CrowdOutputNode,

        CrowdManager_WanderBehaviorNode,

        CrowdManager_ObjectPointScatterNode,
        CrowdManager_PointNode,
        CrowdManager_PointViewer,
        CrowdManager_PointJoin,
    ]