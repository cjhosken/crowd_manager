from ..preferences import getUserPreferences, desaturate

class CrowdManagerBaseNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'CrowdNodeTree'

    node_type = None

    # Functions subclasses can override
    ######################################

    def draw_buttons(self, context, layout):
        pass

    def execute(self, context):
        pass

    def update(self):
        if len(self.outputs) > 0:
            self.link_update()

    # Don't override these functions
    ######################################

    def __init__(self):
        self.name = self.bl_label
        self.label = self.bl_label
        if getUserPreferences().use_node_colors:
            self.use_custom_color = True
            self.color = self.getNodeColoring()
        else:
            self.use_custom_color = False

    def draw_label(self):
        return self.name
    
    def property_changed(self, context):
        self.id_data.update()
        self.update()

    def update_socket(self, context):
        self.link_update()
    
    def link_update(self):
        if len(self.outputs) > 0: 
            for o in self.outputs:
                if len(o.links) > 0:
                    for l in o.links:
                        l.to_node.update
    
    def insert_link(self, link):
        if type(link.to_socket) != type(link.from_socket):
            link.is_valid = False
    
    def get_linked_node(self, socket_id=0, link_id=0):
        if socket_id < len(self.inputs):
            link = self.inputs[socket_id]
            if link.is_linked and len(link.links) > 0 and link.links[link_id].is_valid:
                node = link.links[link_id].from_node
                return node
        return None
    
    def get_linked_nodes(self, socket_id=0):
        nodes = []
        if socket_id < len(self.inputs):
            link = self.inputs[socket_id]
            if link.is_linked and len(link.links) > 0:
                for l in link.links:
                    if l.is_valid:
                        nodes.append(l.from_node)
                if len(nodes) > 0:
                    return nodes
        return None

    # Extra Utilities
    ####################################################

    def getNodeColoring(self):
        type_id = ["object", "collection", "point", "behavior", "agent", "crowd"].index(self.node_type)
        prefs = getUserPreferences()
        color = desaturate([
            prefs.object_node_color,
            prefs.collection_node_color,
            prefs.point_node_color,
            prefs.behavior_node_color,
            prefs.agent_node_color,
            prefs.crowd_node_color
        ][type_id], prefs.node_saturation)

        return color
