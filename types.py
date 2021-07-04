import json
import bpy

class CrowdManager_Point:
    location = [0, 0, 0]
    rotation = [0, 0, 0]

    def __init__(self, loc, rot):
        self.location = loc
        self.rotation = rot

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class CrowdManager_Agent:
    _id = 0
    _ob = None
    _code = ""
    _bLoc = [0.0, 0.0, 0.0]
    _bRot = [0.0, 0.0, 0.0]
    _loc = [0.0, 0.0, 0.0]
    _rot = [0.0, 0.0, 0.0]

    def __init__(self, code, pnt, id):
        print(pnt)
        self._id = id
        self._code = code
        self._bLoc = pnt[0]
        self._bRot = pnt[1]
        self._ob = self.vis()

    def vis(self):
        col = CrowdManager_Agent.getAgentCollection()
        return CrowdManager_Agent.addAgentToCollection(self, col)

    def update(self):
        self.exec_code()
        self._ob.location = self._bLoc
        self._ob.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_current)

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
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)