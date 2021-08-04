import bpy
from ..base_node import CrowdManager_BaseNode

class CrowdManager_CrowdNode(bpy.types.Node, CrowdManager_BaseNode):
    bl_idname = 'CrowdManager_CrowdNode'
    bl_label = 'Crowd'

    node_types = ["crowd"]

    settings : bpy.props.EnumProperty(
        items=[
            ("obj", "Object", ""),
            ("col", "Collection", "")
        ],
        update=CrowdManager_BaseNode.property_changed
    )

    def init(self, context):
        super().__init__()
        self.inputs.new('CrowdManager_AgentSocketType', "Agents")
        self.inputs.new('CrowdManager_ObjectSocketType', "Object")
        self.inputs.new('CrowdManager_CollectionSocketType', "Collection")
        self.hide_links()
        

    def draw_buttons(self, context, layout):
        layout.prop(self, "settings", text="")

    def hide_links(self):
        if self.settings == "obj":
            self.inputs[1].hide = False
            self.inputs[1].enabled = True
            self.inputs[2].hide = True
            self.inputs[2].enabled = False
        elif self.settings == "col":
            self.inputs[1].hide = True
            self.inputs[1].enabled = False
            self.inputs[2].hide = False
            self.inputs[2].enabled = True
    
    def edit(self):
        self.hide_links()
        crowd_collection = getCrowdCollection()
        node0 = self.get_input_node(0)
        node1 = self.get_input_node(1)
        node2 = self.get_input_node(2)

        if len(crowd_collection.objects) > 0:
            for obj in crowd_collection.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)

        if node0 is not None:
            ob = []
            agents = node0.outputs[0].agents

            if self.settings == "obj":
                if node1 is not None and node1.outputs[0].object is not None: 
                        ob = [node1.outputs[0].object]
            elif self.settings == "col":
                if node2 is not None and node2.outputs[0].collection is not None:
                    for obj in node2.outputs[0].collection.objects:
                        ob.append(obj)

            if (self.settings == "obj" and node1 is not None) or (self.settings == "col" and node2 is not None):
                if len(agents) > 0 and len(ob) > 0:
                    obidx = 0
                    for idx, agent in enumerate(agents):
                        cur_ob = ob[obidx]
                        link = bpy.data.objects.get(f"AGENT_{idx}" + "_" + cur_ob.name)
                        if link is None:
                            link = bpy.data.objects.new(f"AGENT_{idx}" + "_" + cur_ob.name, cur_ob.data)
                        
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
                        
                        obidx += 1

                        if obidx >= len(ob):
                            obidx = 0
            else:
                if len(crowd_collection.objects) > 0:
                    for a in crowd_collection.objects:
                        bpy.data.objects.remove(a, do_unlink=True)     

            self.linked_update();                 
        
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