from ..types import CM_DataType
class CM_Point(CM_DataType):
    location = [0,0,0]
    rotation = [0,0,0]

    def __init__(self, loc=[0,0,0], rot=[0,0,0], dict=None):
        if dict is None:
            self.location = loc
            self.rotation = rot
        else:
            self.fromDict(dict)


    def set(self, loc=None, rot=None):
        if loc is not None:
            self.location = loc
        if rot is not None:
            self.rotation = rot
    
    def toDict(self):
        return {
            "location" : self.location,
            "rotation" : self.rotation
        }
    
    def copy(self):
        return CM_Point(self.location[:], self.rotation[:])

    def fromDict(self, dict):
        self.location = dict["location"]
        self.rotation = dict["rotation"]

class CM_PointList(CM_DataType):
    points = []

    def __init__(self, pnts = [], dict=None):
        if dict is None:
            self.points = pnts
        else:
            self.fromDict(dict)

    def add(self, pnt):
        self.points.append(pnt)
    
    def insert(self, pnt, idx):
        self.points.insert(idx, pnt)
    
    def remove(self, idx):
        self.points.remove(idx)

    def get(self, idx):
        return self.points.copy(idx)

    def fromDict(self, dict):
        self.points = []
        for p in dict:
            self.points.append(CM_Point(dict=p))
    
    def toDict(self):
        dict = []
        if len(self.points) > 0:
            for p in self.points:
                dict.append(p.toDict())
        return dict