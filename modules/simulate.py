from modules.agent import Agent
import bpy
from bpy.types import Operator

class CrowdManager_OT_Simulate(Operator):
    bl_label = "Simulate Crowds"
    bl_idname = "crowdmanager.simulate"
    bl_description = "Simulates crowd agents."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        agents = context.scene.crowdmanager_props.agents
        agent_collection = Agent.getAgentCollection()

        context.scene.frame_set(context.scene.frame_start)
        for a in agents:
            a.reset()

        while context.scene.frame_current <= context.scene.frame_end:
            print(context.scene.frame_current)
            for a in agents:
                a.update()
            
            context.scene.frame_set(context.scene.frame_current + 1)

        return {'FINISHED'}

class CrowdManager_OT_ClearSimulations(Operator):
    bl_label = "Simulate Crowds"
    bl_idname = "crowdmanager.desimulate"
    bl_description = "Simulates crowd agents."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        agents = context.scene.crowdmanager_props.agents
        agent_collection = Agent.getAgentCollection()

        context.scene.frame_set(context.scene.frame_start)
        
        for i, agent in enumerate(agent_collection.objects):
            context.view_layer.objects.active = agent
            context.active_object.animation_data_clear()
            agent.animation_data_clear()
            agent.location = agents[i - 1]._baseLocation
            agents[i - 1]._location = agents[i - 1]._baseLocation

            agent.rotation_euler = agents[i - 1]._baseRotation
            agents[i - 1]._rotation = agents[i - 1]._baseRotation

        agent_collection = Agent.getAgentCollection()
        return {'FINISHED'}
        
