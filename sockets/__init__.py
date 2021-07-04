from .object_socket import CrowdManager_ObjectSocket
from .collection_socket import CrowdManager_CollectionSocket
from .crowd_socket import CrowdManager_CrowdSocket
from .behavior_socket import CrowdManager_BehaviorSocket
from .point_socket import CrowdManager_PointSocket

socket_classes = [
    CrowdManager_ObjectSocket,
    CrowdManager_CollectionSocket,
    CrowdManager_CrowdSocket,
    CrowdManager_PointSocket,
    CrowdManager_BehaviorSocket,
    ]