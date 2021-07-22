import json
from bpy.props import BoolProperty, StringProperty
from ..preferences import getUserPreferences, desaturate

class CrowdManager_BaseNode:

    # Properties
    ######################################
    node_id : StringProperty(default="")
    broken : BoolProperty(default=False)
    linked : BoolProperty(default=False)
    node_types = []


    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'crowdmanager_node_tree'


    # Functions subclasses can override
    ######################################

    def draw_buttons(self, context, layout):
        pass

    def execute(self, context):
        pass

    def update(self):
        '''Dont use this, use edit() instead.'''
        '''Only use update for input nodes'''

    def edit(self):
        pass

    # Don't override these functions
    ######################################

    def __init__(self):
        self.name = self.bl_label
        self.label = self.bl_label
        self.node_id = json.dumps([str(self.name), str(self.id_data.name)])
        self.setNodeColoring()
    
    def draw_label(self):
        return self.name

    def property_changed(self, context=None):
        self.id_data.update()
        self.edit()
        self.linked_update()

    def linked_update(self):
        for o in self.outputs:
            if o.is_linked:
                if len(o.links) > 0:
                    for l in o.links:
                        if l.is_valid:
                            l.to_node.edit()
                            l.to_node.linked_update()
    
    def get_input_node(self, idx=None, multi=False):
        nodes = []
        if idx is None:
            for i in self.inputs:
                if i.is_linked:
                    if len(i.links) > 0:
                        for l in i.links:
                            if l.is_valid:
                                if l.from_node.outputs[0].bl_idname == l.to_node.inputs[0].bl_idname:
                                    nodes.append(l.from_node)

            return nodes
        else:
            if len(self.inputs) > idx:
                i = self.inputs[idx]
                if i.is_linked:
                    if len(i.links) > 0:
                        if multi:
                            for l in i.links:
                                if l.is_valid:
                                    if l.from_node.outputs[0].bl_idname == l.to_node.inputs[0].bl_idname:
                                        return i.links[0].from_node
                        else:
                            if i.links[0].is_valid:
                                if i.links[0].from_node.outputs[0].bl_idname == i.links[0].to_node.inputs[idx].bl_idname:
                                    return i.links[0].from_node

        return None

    def free(self):
        self.linked_update()

    def update(self):
        for o in self.outputs:
            if o.links:
                if not self.linked:
                    self.linked = True
                    self.edit()
                    self.linked_update()
            else:
                if self.linked:
                    self.linked = False
                    self.edit()
                    self.linked_update()


    # Extra Utilities
    ####################################################

    def getNodeColoring(self):
        type_id = ["object", "collection", "point", "behavior", "agent", "crowd"].index(self.node_types[0])
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

    def setNodeColoring(self):
        if getUserPreferences().use_node_colors:
            self.use_custom_color = True
            self.color = self.getNodeColoring()
        else:
            self.use_custom_color = False