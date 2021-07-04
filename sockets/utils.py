import time, ast

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

# STRING CONVERSION UTILS

def point_list_to_string(lst):
	out = ""
	out += "["
	for idx, pnt in enumerate(lst):
		lc = pnt[0]
		rt = pnt[1]
		out += f"[({lc[0]}, {lc[1]}, {lc[2]}), ({rt[0]}, {rt[1]}, {rt[2]})]"
		if idx != len(lst) - 1:
			out+= ", "
	out += "]"
	return out

def string_to_point_list(st):
	lst = ast.literal_eval(st)
	return lst

def string_to_list(st):
	lst = ast.literal_eval(st)
	return lst