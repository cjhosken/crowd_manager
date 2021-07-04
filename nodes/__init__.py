from .node_tree import classes as node_tree_classes
from .object.object_input_node import CrowdManager_ObjectInputNode
from .object.collection_input_node import CrowdManager_CollectionInputNode
from .object.collection_to_object_node import CrowdManager_CollectionToObjectNode
from .object.object_to_collection_node import CrowdManager_ObjectToCollectionNode

from .crowd.crowd_node import CrowdManager_CrowdNode
from .crowd.crowd_output_node import CrowdManager_CrowdOutputNode

from .behavior.wander_behavior_node import CrowdManager_WanderBehaviorNode

from.point.object_point_scatter_node import CrowdManager_ObjectPointScatterNode

node_classes = node_tree_classes + [
        CrowdManager_ObjectInputNode,
        CrowdManager_CollectionInputNode,
        CrowdManager_CollectionToObjectNode,
        CrowdManager_ObjectToCollectionNode,
        
        CrowdManager_CrowdNode,
        CrowdManager_CrowdOutputNode,

        CrowdManager_WanderBehaviorNode,

        CrowdManager_ObjectPointScatterNode
    ]