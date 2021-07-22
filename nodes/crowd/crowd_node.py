import bpy
import json
from bpy.props import *
from ..base_node import CM_BaseNode

class CM_CrowdNode(bpy.types.Node, CM_BaseNode):
    bl_idname = 'CM_CrowdNode'
    bl_label = 'Crowd'

    node_type = ["crowd"]

    def init(self, context):
        super().__init__()
        self.inputs.new('CM_AgentSocketType', "Agents")
        self.inputs.new('CM_ObjectSocketType', "Object")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        crowd_collection = getCrowdCollection()
        node0 = self.get_input_node(0)
        node1 = self.get_input_node(1)

        if node0 is not None:
            agents = node0.outputs[0].agents

            if node1 is not None and node1.outputs[0].object is not None:
                ob = node1.outputs[0].object

                if len(agents) > 0:
                    for i, ag in enumerate(agents):
                        lk = bpy.data.objects.get(f"AGENT_{i}" + "_" + ob.name)
                        if lk is None:
                            lk = bpy.data.objects.new(f"AGENT_{i}" + "_" + ob.name, ob.data)
                        
                            addInstanceToCollection(lk, crowd_collection, i)

                        if ag.simulated:
                            for i, s in enumerate(ag.sim):
                                lk.location = s.location
                                lk.keyframe_insert(data_path="location", frame = i + ag.sim_start)
                        else:
                            lk.location = ag.sim[0].location
            else:
                if len(crowd_collection.objects) > 0:
                    for a in crowd_collection.objects:
                        bpy.data.objects.remove(a, do_unlink=True)                      
        
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