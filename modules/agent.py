import bpy

# AGENT_id

class Agent():
    def __init__(self, id, bl, br):
        self._id = id
        self._baseLocation = bl
        self._baseRotation = br
        self._location = self._baseLocation
        self._rotation = self._baseRotation

    def build(self):
        col = Agent.getAgentCollection()
        Agent.addAgentToCollection(self, col)

    def setLocation(self, vec):
        self._baseLocation = vec

    def setRotation(self, vec):
        self._baseRotation = vec

    def reset(self):
        self._location = self._baseLocation
        self._rotation = self._baseRotation
        ob = bpy.data.objects.get(f"AGENT_{self._id}")
        ob.location = self._location
        ob.rotation_euler = self._rotation
    
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

    def ReloadAgents():
        bpy.context.scene.crowdmanager_props.agents
        agent_collection = bpy.context.scene.crowdmanager_props.agent_collection

        if len(bpy.context.scene.crowdmanager_props.agents) != len(agent_collection.objects):
            bpy.context.scene.crowdmanager_props.agents = []
            for i, agent in enumerate(agent_collection.objects):
                ag = Agent(i, agent.location, agent.rotation_euler)
                bpy.context.scene.crowdmanager_props.agents.append(ag)
