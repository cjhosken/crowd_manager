import time, ast

def updatePointNodeSocketValue(lock, passedSelf, passedValue, passedSleepTime):
	time.sleep(passedSleepTime)
	try:
		if passedSelf.points != passedValue:
			passedSelf.points = passedValue
		passedSelf.points = passedValue
	except AttributeError:
		pass
		

	
def updateParameter(self,context):
	try:
		scene = context.scene
	except:
		scene = None
	if scene != None:
		#print(self.value)
		pass