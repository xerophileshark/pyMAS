from abc import ABC, abstractmethod
from typing import List

class Agent(ABC):
    def __init__(self, f = None, index=0):
        if f != None:
            self.f = f
        self.index = index
    
    @abstractmethod
    def f(self, t):
        pass

class MAS:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
    
    def show_indexes(self):
        for a in self.agents:
            print(a.index)
    
    def show_ids(self):
        for a in self.agents:
            print(id(a))
            
# %%

class MyAgent(Agent):
    def f():
        print("I am an implemented version of f()")
        
# %%      
        
listOfAgents = []
for i in range(5):
    listOfAgents.append( MyAgent(index=i) )
    print(id(listOfAgents[i]))
    
print('-------------------------------')

mas = MAS(agents=listOfAgents)

mas.show_ids()