import bpy

class Agent():
    def __init__(self, code, pnt, id):
        self._id = id
        self._bLoc, self._loc = pnt.location
        self._bRot, self._rot = pnt.rotation
        self.vis()

    def vis(self):
        col = Agent.getAgentCollection()
        Agent.addAgentToCollection(self, col)

    def update(self):
        pass

    def addAgentToCollection(agent, col):
        if len(col.objects) > 0:
            for a in col.objects:
                if a.name == f"AGENT_{agent._id}":
                    bpy.data.objects.remove(a, do_unlink=True)
                    break

        e = bpy.data.objects.new("empty", None)
        col.objects.link(e)

        e.name = f"AGENT_{agent._id}"
        e.empty_display_size = 1
        e.empty_display_type = 'SPHERE'
        agent._baseLocation = e.location
        agent._baseRotation = e.rotation_euler
        agent._location = agent._baseLocation
        agent._rotation = agent._baseRotation
    
    def getAgentCollection():
        collection = bpy.data.collections.get("GRP_AgentCollection")

        if collection is None:
            collection = bpy.data.collections.new("GRP_AgentCollection")
            bpy.context.scene.collection.children.link(collection)

        return collection