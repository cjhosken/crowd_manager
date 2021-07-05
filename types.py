import json
import bpy

class CrowdManager_Point:
    location = [0, 0, 0]
    rotation = [0, 0, 0]

    def __init__(self, loc, rot):
        self.location = loc
        self.rotation = rot

    def toDict(self):
        return {
            "location" : self.location,
            "rotation" : self.rotation
        }

class CrowdManager_Agent:
    _id = 0
    _ob = None
    _code = ""
    _bLoc = [0.0, 0.0, 0.0]
    _bRot = [0.0, 0.0, 0.0]
    _loc = [0.0, 0.0, 0.0]
    _rot = [0.0, 0.0, 0.0]

    def __init__(self, code, pnt, id, obname=None):
        self._id = id
        self._code = code
        self._bLoc = pnt["location"]
        self._bRot = pnt["rotation"]
        self._loc = self._bLoc
        self._rot = self._bRot
        if obname is None:
            self._ob = self.vis()
        else:
            self._ob = bpy.data.objects.get(obname)

    def vis(self):
        col = CrowdManager_Agent.getAgentCollection()
        return CrowdManager_Agent.addAgentToCollection(self, col)

    def update(self):
        self.exec_code()
        self._ob.location = self._loc
        self._ob.keyframe_insert(data_path="location", frame=bpy.context.scene.frame_current)
 
    def clear(self):
        self._ob.animation_data_clear()
        self._ob.location = self._bLoc
        self._ob.rotation_euler = self._bRot

    def exec_code(self):
        import random
        if len(self._code) > 0:
            d = {}
            exec(self._code, d)
            tmp_loc = d["l"]
            self._loc[0] += tmp_loc[0]
            self._loc[1] += tmp_loc[1]
            self._loc[2] += tmp_loc[2]

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
    
    def toDict(self):
        return {
            "id" : self._id,
            "obname" : self._ob.name,
            "code" : self._code,
            "bLoc" : self._bLoc,
            "bRot" : self._bRot,
            "loc" : self._loc,
            "rot" : self._rot
        }