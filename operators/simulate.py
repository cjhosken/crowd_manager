import bpy
import json

class CM_OT_Simulate(bpy.types.Operator):
    bl_label = "Simulate Crowds"
    bl_idname = "crowdmanager.simulate"
    bl_description = "Simulates crowd agents."
    bl_options = {"REGISTER", "UNDO"}

    node_data : bpy.props.StringProperty(name="Node", default="")

    def execute(self, context):
        wm = context.window_manager
        tot = 100
        data = json.loads(self.node_data)
        node = bpy.data.node_groups[data[1]].nodes[data[0]]

        agents = node.outputs[0].agents
        code = node.code
        print(code)

        context.scene.frame_set(context.scene.frame_start)

        f = 0
        e = context.scene.frame_end - context.scene.frame_start
        wm.progress_begin(0, tot)
        while context.scene.frame_current <= context.scene.frame_end:
            for AGENT in agents:
                AGENT.simulated = True
                if context.scene.frame_current == context.scene.frame_start:
                    AGENT.sim_start = context.scene.frame_start
                else:
                    if code is not None and len(code) > 0:
                        AGENTS = agents
                        AGENT = AGENT
                        FRAME = context.scene.frame_current
                        LAST_SIM = AGENT.sim[-1]

                        var = {
                            "AGENTS": agents,
                            "AGENT": AGENT,
                            "FRAME": context.scene.frame_current,
                            "LAST_SIM": AGENT.sim[-1]
                        }
                        exec(code, var)

                        out = var["OUTPUT"]
                        s = AGENT.sim.add()
                        s.location = out[0]
                    else:
                        s = AGENT.sim.add()

                print(f"SIMULATING FRAME {context.scene.frame_current} - {((f / e)*100):.2f}%")
                wm.progress_update(f)
            
            context.scene.frame_set(context.scene.frame_current + 1)
            f += 1

        wm.progress_end()
        context.scene.frame_set(context.scene.frame_start)

        node.simulated = True
        node.linked_update()
        return {'FINISHED'}

class CM_OT_DeSimulate(bpy.types.Operator):
    bl_label = "Clear Simulated Crowds"
    bl_idname = "crowdmanager.desimulate"
    bl_description = "Clears crowd agents simulation."
    bl_options = {"REGISTER", "UNDO"}

    node_data : bpy.props.StringProperty(name="Node", default="")

    def execute(self, context):
        data = json.loads(self.node_data)
        node = bpy.data.node_groups[data[1]].nodes[data[0]]

        agents = node.outputs[0].agents

        for a in agents:
            tmp = a.sim[0]
            a.sim.clear()
            a.sim.add()
            a.location = tmp.location
            a.sim_start = context.scene.frame_start
            a.simulated = False


        node.simulated = False
        node.linked_update()
        return {'FINISHED'}

simulate_classes = [CM_OT_Simulate, CM_OT_DeSimulate]