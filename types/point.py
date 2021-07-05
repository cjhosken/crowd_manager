from ..types import CM_DataType

class CM_PVec(CM_DataType):
    location = [0,0,0]
    rotation = [0,0,0]

    def __init__(self, loc=[0,0,0], rot=[0,0,0], dict=None):
        if dict is None:
            self.location = loc
            self.rotation = rot
        else:
            self.fromDict(dict)
    
    def toDict(self):
        return {
            "location" : self.location,
            "rotation" : self.rotation
        }
    
    def fromDict(self, dict):
        self.location = dict["location"]
        self.rotation = dict["rotation"]

class CM_Point(CM_DataType):
    location = [0,0,0]
    rotation = [0,0,0]
    sim = []
    sim_start = 0

    def __init__(self, loc=[0,0,0], rot=[0,0,0], sim=[], sim_start=0):
        self.location = loc
        self.rotation = rot
        self.sim = sim
        self.sim_start = sim_start
        self.is_simulated = len(sim) > 0

    def set(self, loc=None, rot=None, sim=None, sim_start=None):
        if loc is not None:
            self.location = loc
        if rot is not None:
            self.rotation = rot
        if sim is not None:
            self.sim = sim
            self.is_simulated = len(sim) > 0
        if sim_start is not None:
            self.sim_start = sim_start
    
    def toDict(self):
        dict = {
            "origin" : CM_PVec(self.location, self.rotation).toDict(),
            "is_simulated" : len(self.sim) > 0,
            "sim_data": {},
            "sim_start" : self.sim_start,
        }

        for p in self.sim:
            dict["sim_data"].append(p.toDict())

    def fromDict(self, dict):
        self.location, self.rotation = dict["origin"]
        self.sim_start = dict["sim_start"]
        self.is_simulated = dict["is_simulated"]

        for p in dict["sim_data"]:
            self.sim.append(CM_Point(p))


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
            self.points.append(CM_Point(p))
    
    def toDict(self):
        dict = []
        if len(self.points) > 0:
            for p in self.points:
                dict.append(p.toDict())
        return dict