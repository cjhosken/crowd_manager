import bpy
import gpu
import bgl
from gpu_extras.batch import batch_for_shader

SpaceView3D = bpy.types.SpaceView3D
handlers = bpy.app.handlers
cm_frame_handle = None
cm_draw_handle = None

cm_draw_nodes_list = {}

def cm_frame_handler(scene, depsgraph):
    cm_draw_handler()

def get_viewer_nodes():
    nodes = []
    for n in bpy.data.node_groups:
        if n.bl_idname == "crowdmanager_node_tree":
            for node in n.nodes:
                if "viewer" in node.node_type:
                    nodes.append(node)
    
    return nodes

def cm_draw_handler():
    if bpy.context and bpy.context.area:
        shader = gpu.shader.from_builtin("3D_SMOOTH_COLOR")
        points = []
        colors = []

        nodes = get_viewer_nodes()

        for n in nodes:
            if "point" in n.node_type:
                if n.GL_POINTS is not None and len(n.GL_POINTS) > 0:
                    for p in n.GL_POINTS:
                        points.append(p.location)
                        colors.append(n.GL_COLOR)

            elif "agent" in n.node_type:
                if n.GL_AGENTS is not None and len(n.GL_AGENTS) > 0:
                    for a in n.GL_AGENTS:
                        if a.simulated == True:
                            points.append(a.sim[bpy.context.scene.frame_current - a.sim_start].location)
                            colors.append(n.GL_COLOR)
                        else:
                            points.append(a.sim[0].location)
                            colors.append(n.GL_COLOR)
            else:
                pass

        
        batch = batch_for_shader(shader, 'POINTS', {'pos': points, 'color': colors})
        bgl.glPointSize(10)
        shader.bind()
        batch.draw(shader)


def register():
    global cm_frame_handle, cm_draw_handle
    cm_draw_handle = SpaceView3D.draw_handler_add(cm_draw_handler, (), 'WINDOW', 'POST_VIEW')
    cm_frame_handle = handlers.frame_change_post.append(cm_frame_handler)

def unregister():
    global cm_frame_handle, cm_draw_handle

    if cm_frame_handle in handlers.frame_change_post:
        handlers.frame_change_post.remove(cm_frame_handle)
    
    SpaceView3D.draw_handler_remove(cm_draw_handle, 'WINDOW')