from .point_socket import CrowdManager_PointSocket, CrowdManager_PointProperty
from .object_socket import CrowdManager_ObjectSocket
from .collection_socket import CrowdManager_CollectionSocket
from .agent_socket import CrowdManager_AgentSocket, CrowdManager_AgentProperty
from .behavior_socket import CrowdManager_BehaviorSocket

socket_classes = [
    CrowdManager_PointProperty,
    CrowdManager_PointSocket,

    CrowdManager_ObjectSocket,
    CrowdManager_CollectionSocket,

    CrowdManager_BehaviorSocket,

    CrowdManager_AgentProperty,
    CrowdManager_AgentSocket,
    ]