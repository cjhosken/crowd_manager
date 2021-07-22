from .point_socket import CM_PointSocket, CM_PointProperty
from .object_socket import CM_ObjectSocket
from .agent_socket import CM_AgentSocket, CM_AgentProperty
from .behavior_socket import CM_BehaviorSocket

socket_classes = [
    CM_PointProperty,
    CM_PointSocket,

    CM_ObjectSocket,

    CM_BehaviorSocket,

    CM_AgentProperty,
    CM_AgentSocket,
    ]