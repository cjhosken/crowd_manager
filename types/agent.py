from ..types import CM_DataType
from .point import CM_Point

class CM_Agent(CM_DataType):
    origin = CM_Point()
    sim_data = []
    sim_start = 0
    simulated = False
    code = ""

    def __init__(self, origin=CM_Point(), sim_data=[], sim_start=0, code="", dict=None):
        if dict is None:
            self.origin = origin
            self.sim_data = sim_data
            self.sim_start = sim_start
            self.simulated = len(sim_data) > 0
            self.code = code
        else:
            self.fromDict(dict)

    def fromDict(self, dict):
        self.origin = CM_Point(dict=dict["origin"])
        self.sim_start = dict["sim_start"]
        self.simulated = dict["simulated"]
        self.sim_data = []
        self.code = dict["code"]
        if self.simulated:
            for d in dict["sim_data"]:
                self.sim_data.append(CM_Point(d))

    def sim(self, context):
        if context.scene.frame_current == self.sim_start:
            self.sim_data.append(self.origin)
        else:
            last = self.sim_data[-1]
            cp = last
            if len(self.code) > 0:
                d = {}
                exec(self.code, d)
                tmp_loc = d["l"]
                out_loc = last.location
                out_loc[0] += tmp_loc[0]
                out_loc[1] += tmp_loc[0]
                out_loc[2] += tmp_loc[0]
                cp = CM_Point(loc=out_loc)
            self.sim_data.append(cp)
        self.simulated = True


    def toDict(self):
        dict = {
            "origin": self.origin.toDict(),
            "sim_start": self.sim_start,
            "simulated": self.simulated,
            "sim_data": [],
            "code": self.code
        }

        for d in self.sim_data:
            dict["sim_data"].append(d.toDict())
        return dict
        


class CM_AgentList(CM_DataType):
    agents = []
    simulated = False

    def __init__(self, agents = [], dict=None):
        if dict is None:
            self.agents = agents
            for agent in self.agents:
                if not agent.simulated:
                    self.simulated = False
                    break
            else:
                self.simulated = True
        else:
            self.fromDict(dict)

    def add(self, pnt):
        self.agents.append(pnt)
    
    def insert(self, pnt, idx):
        self.agents.insert(idx, pnt)
    
    def remove(self, idx):
        self.agents.remove(idx)

    def get(self, idx):
        return self.agents.copy(idx)

    def fromDict(self, dict):
        self.agents = []
        self.simulated = dict["simulated"]
        for a in dict["agents"]:
            self.agents.append(CM_Agent(dict=a))
    
    def toDict(self):
        dict = {
            "agents" : [],
            "simulated" : self.simulated
        }
        if len(self.agents) > 0:
            for a in self.agents:
                dict["agents"].append(a.toDict())
        return dict