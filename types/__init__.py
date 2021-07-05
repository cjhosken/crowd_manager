import json

class CM_DataType:
    def __init__(self, dict=None):
        pass

    def toDict(self):
        return {}
    
    def fromDict(self, dict):
        pass
    
    def toJSON(self):
        return json.dumps(self.toDict())

    def fromJSON(js):
        return json.loads(js)