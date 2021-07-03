import bpy
import threading, time
from bpy.props import IntProperty, FloatProperty, StringProperty, FloatVectorProperty, CollectionProperty, EnumProperty
from bpy.types import NodeTree, Node, NodeSocket
from ..preferences import getUserPreferences

############################################################################
# Thread processing for parameters that are invalid to set in a DRAW context.
# By performing those operations in these threads we can get around the lock within a draw event.
# This is fairly abusive to the system and may result in instability of operation.
# Then again as long as you trap for stale data it just might work..?
# For best result keep the sleep time as quick as possible...no long delays here.
############################################################################
def updateNodeSocketValue(lock, passedSelf, passedValue, passedSleepTime):
	time.sleep(passedSleepTime) # Feel free to alter time in seconds as needed. 
	if passedSelf.value != passedValue:
		# New value needs to be assigned.
		passedSelf.value = passedValue

############################################################################
# Update change in my value.
############################################################################		
def updateParameter(self,context):
	try:
		scene = context.scene
	except:
		scene = None
	if scene != None:
		#print(self.value)
		pass
		
# Custom socket type
class CrowdManager_CollectionSocket(NodeSocket):
	'''Custom node socket type'''			# Description string
	bl_idname = 'CrowdManager_CollectionSocketType'		# Optional identifier string. If not explicitly defined, the python class name is used.
	bl_label = 'Collection Socket'				# Label for nice name display

	collection : bpy.props.PointerProperty(name="Colleciton", type=bpy.types.Collection, update=updateParameter)

	# Optional function for drawing the socket input value
	def draw(self, context, layout, node, text):
		pass
		#if self.is_linked:
		#	try:
		#		v = self.node.inputs[0].links[0].from_socket.node.inputs[0].object
		#		result = str(int(v))	
		#		
		#		# We want to execute this next line right now but Blender has a lock in place.
		#		#self.value = v
		#		# Launch a delayed thread to set the value that would generate an error if issued now.
		#		lock = threading.Lock()
		#		lock_holder = threading.Thread(target=updateNodeSocketValue, args=(lock,self,v,0.02), name='Update_Node_Socket_Value')
		#		lock_holder.setDaemon(True)
		#		lock_holder.start()
		#	except:
		#		result = text
		#
		#else:
		layout.label(text=text)

	# Socket color
	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.collection_node_color
		return (color[0], color[1], color[2], 1)
