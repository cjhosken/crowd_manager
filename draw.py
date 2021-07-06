from .nodes.agent.agent_viewer_node import GL_AGENTS
from .nodes.point.point_viewer_node import GL_POINTS
import bpy
import gpu
import bgl
from gpu_extras.batch import batch_for_shader

viewhandle = None
framehandle = None

def viewport_draw():
    if bpy.context and bpy.context.area:
        shader = gpu.shader.from_builtin("3D_SMOOTH_COLOR")
        points = []
        colors = []
        for n in GL_POINTS:
            points += n[1]
            colors += n[2]
        
        for a in GL_AGENTS:
            points += a[1]
            colors += a[2]
        
        batch = batch_for_shader(shader, 'POINTS', {'pos': points, 'color': colors})
        bgl.glPointSize(10)
        shader.bind()
        batch.draw(shader)

def frame_handler(scene, depsgraph):
    for n in bpy.data.node_groups:
        if n.bl_idname == "crowdmanager_node_tree":
            for node in n.nodes:
                if node.bl_idname == "CrowdManager_AgentViewerNode":
                    node.edit()
