import bpy
from ..base_node import CrowdManager_BaseNode

class CrowdManager_CrowdNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_CrowdNode'
    bl_label = 'Crowd'

    node_types = ["crowd"]

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_AgentSocketType', "Agents")
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")

    def draw_buttons(self, context, layout):
        pass
    
    def edit(self):
        crowd_collection = getCrowdCollection()
        node0 = self.get_input_node(0)
        node1 = self.get_input_node(1)

        if len(crowd_collection.objects) > 0:
            for obj in crowd_collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)

        if node0 is not None:
            agents = node0.outputs[0].agents

            if node1 is not None and node1.outputs[0].object is not None:
                ob = node1.outputs[0].object

                if len(agents) > 0:
                    for idx, agent in enumerate(agents):
                        link = bpy.data.objects.get(f"AGENT_{idx}" + "_" + ob.name)
                        if link is None:
                            link = bpy.data.objects.new(f"AGENT_{idx}" + "_" + ob.name, ob.data)
                        
                            addInstanceToCollection(link, crowd_collection, idx)

                        if agent.simulated:
                            for i, s in enumerate(agent.sim):
                                link.location = s.location
                                link.rotation_euler = s.rotation
                                link.keyframe_insert(data_path="location", frame = i + agent.sim_start)
                                link.keyframe_insert(data_path="rotation_euler", frame = i + agent.sim_start)
                        else:
                            link.location = agent.sim[0].location
                            link.rotation_euler = agent.sim[0].rotation
            else:
                if len(crowd_collection.objects) > 0:
                    for a in crowd_collection.objects:
                        bpy.data.objects.remove(a, do_unlink=True)                      
        
def addInstanceToCollection(instance, col, idx):
    if len(col.objects) > 0:
        for a in col.objects:
            if f"AGENT_{idx}" in a.name:
                bpy.data.objects.remove(a, do_unlink=True)
                break

    col.objects.link(instance)

def getCrowdCollection():
    collection = bpy.data.collections.get("GRP_CrowdCollection")

    if collection is None:
        collection = bpy.data.collections.new("GRP_CrowdCollection")
        bpy.context.scene.collection.children.link(collection)
            
    return collection