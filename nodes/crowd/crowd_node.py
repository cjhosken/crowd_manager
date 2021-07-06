import bpy
import json
from bpy.props import *
from ..base_node import CrowdManagerBaseNode
from ...types.agent import CM_Agent, CM_AgentList
from ...types.point import CM_Point, CM_PointList

class CrowdManager_CrowdNode(bpy.types.Node, CrowdManagerBaseNode):
    bl_idname = 'CrowdManager_CrowdNode'
    bl_label = 'Crowd'

    node_type = "crowd"
    linked : BoolProperty()

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_AgentSocketType', "Agents")
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")

        #self.outputs.new('CrowdManager_CrowdSocketType', "Crowd")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        crowd_collection = getCrowdCollection()
        node0 = self.get_linked_node(0)
        node1 = self.get_linked_node(1)

        if node0 is not None:
            agents = CM_AgentList(dict=CM_AgentList.fromJSON(node0.outputs[0].agents))

            if node1 is not None and node1.outputs[0].object is not None:
                ob = node1.outputs[0].object

                if len(agents.agents) > 0:
                    for i, ag in enumerate(agents.agents):
                        lk = bpy.data.objects.get(f"AGENT_{i}" + "_" + ob.name)
                        if lk is None:
                            lk = bpy.data.objects.new(f"AGENT_{i}" + "_" + ob.name, ob.data)
                        
                            addInstanceToCollection(lk, crowd_collection, i)

                        if len(ag.sim_data) > 0:
                            for d in range(len(ag.sim_data)):
                                lk.location = ag.sim_data[d].location
                                lk.keyframe_insert(data_path="location", frame = d + ag.sim_start)
                        else:
                            lk.location = ag.origin.location
            else:
                if len(crowd_collection.objects) > 0:
                    for a in crowd_collection.objects:
                        bpy.data.objects.remove(a, do_unlink=True)

    def update(self):
        for i in self.inputs:
            if i.links:
                if not self.linked:
                    self.edit()
                    self.linked = True
            else:
                if self.linked:
                    self.edit()
                    self.linked = False                        
        
def addInstanceToCollection(instance, col, i):
    if len(col.objects) > 0:
        for a in col.objects:
            if f"AGENT_{i}" in a.name:
                bpy.data.objects.remove(a, do_unlink=True)
                break

    col.objects.link(instance)

def getCrowdCollection():
    collection = bpy.data.collections.get("GRP_CrowdCollection")

    if collection is None:
        collection = bpy.data.collections.new("GRP_CrowdCollection")
        bpy.context.scene.collection.children.link(collection)
            
    return collection