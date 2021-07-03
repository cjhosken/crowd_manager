import time

def updateNodeSocketValue(lock, passedSelf, passedValue, passedSleepTime):
	time.sleep(passedSleepTime)
	if passedSelf.value != passedValue:
		passedSelf.value = passedValue
	
def updateParameter(self,context):
	try:
		scene = context.scene
	except:
		scene = None
	if scene != None:
		#print(self.value)
		pass