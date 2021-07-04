import bpy
class Agent():
    def __init__(self, code, pnt, id):
        self._id = id
        self._bLoc = pnt[0]
        self._loc = pnt[0]
        self._bRot = pnt[1]
        self._rot = pnt[0]
        self.vis()

    def vis(self):
        col = Agent.getAgentCollection()
        self.ob = Agent.addAgentToCollection(self, col)

    def update(self):
        self.exec_code()
        self.ob.location = self._loc
        self.ob.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_current)

    def exec_code(self):
        exec(self.code)











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
        e.location = agent._bLoc
        e.rotation_euler = agent._bRot
        return e

    def clearAgentCollection(col):
        if len(col.objects) > 0:
            for a in col.objects:
                bpy.data.objects.remove(a, do_unlink=True)
    
    def getAgentCollection():
        collection = bpy.data.collections.get("GRP_AgentCollection")

        if collection is None:
            collection = bpy.data.collections.new("GRP_AgentCollection")
            bpy.context.scene.collection.children.link(collection)

        return collection