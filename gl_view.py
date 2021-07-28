from .preferences import getUserPreferences
import bpy
import gpu
import math
import bgl
from gpu_extras.batch import batch_for_shader

SpaceView3D = bpy.types.SpaceView3D
handlers = bpy.app.handlers

CROWDMANAGER_FRAME_HANDLE = None
CROWDMANAGER_DRAW_HANDLE = None

CROWDMANAGER_DRAW_NODES_LIST = {}

def get_viewer_nodes():
    nodes = []
    for ntree in bpy.data.node_groups:
        if ntree.bl_idname == "crowdmanager_node_tree":
            for node in ntree.nodes:
                if "viewer" in node.node_types:
                    nodes.append(node)
    
    return nodes

def crowdmanager_draw_handler():
    crowdmanager_gl_draw()

def crowdmanager_frame_handler(scene, depsgraph):
    crowdmanager_gl_draw()

def crowdmanager_gl_draw():
    if bpy.context and bpy.context.area:
        shader = gpu.shader.from_builtin("3D_SMOOTH_COLOR")
        nodes = get_viewer_nodes()
        points = [] 
        colors = []

        for node in nodes:
            if "point" in node.node_types:
                if node.GL_POINTS is not None and len(node.GL_POINTS) > 0:
                    for point in node.GL_POINTS:
                        points.append(point.location)
                        colors.append(node.GL_COLOR)
            

            elif "agent" in node.node_types:
                if node.GL_AGENTS is not None and len(node.GL_AGENTS) > 0:
                    for agent in node.GL_AGENTS:
                        if agent.simulated == True:
                            points.append(agent.sim[bpy.context.scene.frame_current - agent.sim_start - 1].location)
                            colors.append(node.GL_COLOR)
                        else:
                            points.append(agent.sim[0].location)
                            colors.append(node.GL_COLOR)
        
        batch = batch_for_shader(shader, 'POINTS', {'pos': points, 'color': colors})
        bgl.glPointSize(getUserPreferences().point_size)
        bgl.glEnable(bgl.GL_DEPTH_TEST)
        bgl.glEnable(bgl.GL_POLYGON_SMOOTH)
        bgl.glEnable(bgl.GL_BLEND)
        
        shader.bind()
        batch.draw(shader)

def register():
    global CROWDMANAGER_FRAME_HANDLE, CROWDMANAGER_DRAW_HANDLE
    CROWDMANAGER_DRAW_HANDLE = SpaceView3D.draw_handler_add(crowdmanager_draw_handler, (), 'WINDOW', 'POST_VIEW')
    CROWDMANAGER_FRAME_HANDLE = handlers.frame_change_post.append(crowdmanager_frame_handler)

def unregister():
    global CROWDMANAGER_FRAME_HANDLE, CROWDMANAGER_DRAW_HANDLE

    if CROWDMANAGER_FRAME_HANDLE in handlers.frame_change_post:
        handlers.frame_change_post.remove(CROWDMANAGER_FRAME_HANDLE)
    
    SpaceView3D.draw_handler_remove(CROWDMANAGER_DRAW_HANDLE, 'WINDOW')