import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types import CrowdManager_Agent as CM_Agent, CrowdManager_Point as CM_Point

class CrowdManager_PopulateAgentsNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_PopulateAgentsNode'
    bl_label = 'Populate Agents'

    node_type = "crowd"

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_AgentSocketType', "Agents")
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")

        self.outputs.new('CrowdManager_CrowdSocketType', "Crowd")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        crowd_collection = getCrowdCollection()
        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)

        local_agents = []

        if node0 is not None:
            agents = json.loads(node0.outputs[0].agents)["agents"]

            for a in agents:
                ag = CM_Agent(id=a["id"], pnt=CM_Point(a["bLoc"], a["bRot"]).toDict(), code=a["code"], obname=a["obname"])
                local_agents.append(ag)

            if node1 is not None and node1.outputs[0].object is not None:
                ob = node1.outputs[0].object

                if len(local_agents) > 0:
                    for empty in local_agents:
                        base = empty._ob
                        lk = bpy.data.objects.get(base.name + "_" + ob.name)
                        if lk is None:
                            lk = bpy.data.objects.new(base.name + "_" + ob.name, ob.data)
                        
                            addInstanceToCollection(lk, crowd_collection)

                        lk.rotation_euler = base.rotation_euler
                        lk.scale = base.scale
                        lk.parent = base 
            else:
                if len(local_agents) > 0:
                    for empty in local_agents:
                        base = empty._ob
                        for a in crowd_collection.objects:
                            if a.name != base.name:
                                if base.name in a.name:
                                    bpy.data.objects.remove(a, do_unlink=True)
                        
        
def addInstanceToCollection(instance, col):
    if len(col.objects) > 0:
        for a in col.objects:
            if a.name == instance.name:
                bpy.data.objects.remove(a, do_unlink=True)
                break

    col.objects.link(instance)

def getCrowdCollection():
    collection = bpy.data.collections.get("GRP_CrowdCollection")

    if collection is None:
        collection = bpy.data.collections.new("GRP_CrowdCollection")
        bpy.context.scene.collection.children.link(collection)
            
    return collection


            


        