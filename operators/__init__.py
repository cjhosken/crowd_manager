import bpy
import json
from bpy.props import *
from ..types.agent import CM_Agent, CM_AgentList

class CrowdManager_OT_CreateCollection(bpy.types.Operator):
    bl_label = "Create Collection"
    bl_idname = "crowdmanager.create_collection"
    bl_description = "Creates a collection"
    bl_options = {"REGISTER", "UNDO"}

    collection_name : StringProperty(name="Collection Name")

    def execute(self, context):
        collection = bpy.data.collections.get(self.collection_name)

        if collection is None:
            collection = bpy.data.collections.new(self.collection_name)
            bpy.context.scene.collection.children.link(collection)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class CrowdManager_OT_Simulate(bpy.types.Operator):
    bl_label = "Simulate Crowds"
    bl_idname = "crowdmanager.simulate"
    bl_description = "Simulates crowd agents."
    bl_options = {"REGISTER", "UNDO"}

    node_name : bpy.props.StringProperty(name="Node", default="")

    def execute(self, context):
        node = bpy.context.space_data.edit_tree.nodes.get(self.node_name)
        agents = CM_AgentList(dict=CM_AgentList.fromJSON(node.agents))

        context.scene.frame_set(context.scene.frame_start)

        f = 0
        e = context.scene.frame_end - context.scene.frame_start
        while context.scene.frame_current <= context.scene.frame_end:
            for ag in agents.agents:
                if context.scene.frame_current == context.scene.frame_start:
                    ag.sim_start = context.scene.frame_start
                ag.sim(context)
                print(f"SIMULATING FRAME {context.scene.frame_current} - {((f / e)*100):.2f}%")
            
            context.scene.frame_set(context.scene.frame_current + 1)
            f += 1
            
        context.scene.frame_set(context.scene.frame_start)
        agents.simulated = True
        node.agents = agents.toJSON()
        node.outputs[0].agents = node.agents
        return {'FINISHED'}


operator_classes = [CrowdManager_OT_CreateCollection, CrowdManager_OT_Simulate]