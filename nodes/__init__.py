from .node_tree import classes as node_tree_classes
from .object.object_input_node import CrowdManager_ObjectInputNode
from .object.collection_input_node import CrowdManager_CollectionInputNode
from .object.collection_to_object_node import CrowdManager_CollectionToObjectNode
from .object.object_to_collection_node import CrowdManager_ObjectToCollectionNode

node_classes = node_tree_classes + [
        CrowdManager_ObjectInputNode,
        CrowdManager_CollectionInputNode,
        CrowdManager_CollectionToObjectNode,
        CrowdManager_ObjectToCollectionNode,
    ]