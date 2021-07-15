# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 22:16:32 2021

@author: Ali
"""
import numpy as np

from pymas.agent import Agent
from pymas.network import Network
from pymas.dcontroller import Dcontroller
from pymas import mas

# %%      

# Number of inputs & outputs & states of each agent's dynamics & number of agents:
ni=1
no=1
ns=1
numOfAgents = 6

# Create my custom Agent class called MyAgent
class MyAgent(Agent):
    
    # Note: We "can" change the default numbers to fit our dynamics in here:
    def __init__(self, ni=1, no=1, ns=2, f=None, *, tStart=0, \
                 init_states=None, index: int=None):
        # Should call the parent's __init__ to access methods and attributes:
        # *** Pay attention to the positional and non-positional arguments. ***
        Agent.__init__(self, ni, no, ns, f, tStart=tStart, \
                       init_states=init_states, index=index)
    
    # My custom dynamics: Single integrator: x_dot(t) = u(t) => f = u
    def f(self, t, x, u):
        return u

# Create a list of (e.g. three) agents with appropriate indexes (start from 0):  
listOfAgents = []
inits = np.array([[1], [-1], [3], [-3], [5], [-5]])
for i in range(numOfAgents):
    # Define initial states for each agent, randomly:
    # init_states = np.random.rand(ns, 1) * 10
    init_states = inits[i].reshape(ns, 1)
    listOfAgents.append( MyAgent(ni=ni, no=no, ns=ns, tStart=0, \
                                 init_states=init_states, index=i) )

# Create an instance of Network with intended topology:
#   - Define Adjacancy matrix: (Undirected graph of page 31)
A = np.array([[0, 1, 1, 0, 0, 0], 
              [1, 0, 1, 1, 0, 1], 
              [1, 1, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 1],
              [0, 1, 0, 1, 1, 0]]) 
#   - Create the network instance:
net = Network(A, listOfAgents)

# Create a custom distributed control strategy by implementing Dcontroller methods:
class MyDcontroller(Dcontroller):
    
    def __init__(self, net: Network):
        Dcontroller.__init__(self, net)
    
    def rule(self, agent, neighbour):
        return neighbour.stateTrajectHistory[:, -1] - agent.stateTrajectHistory[:, -1]
    
    def controlProtocol(self, agentIndex: int,  t): # Simple sigma protocol
        print("For agent ", agentIndex, "-- t: ", t)
        # # if t == 0 then return zero output vector (since u(0) is 0):
        # if t == self.net.agents[agentIndex].tStart:
        #     return np.zeros(shape=(self.no, 1))
        # Calculate the control input of "agentIndex"-th agent:
        u = np.zeros(shape=(self.no, 1))
        for a in self.net.agents:
            if self.net.areNeighbours(a.index, agentIndex):
                u += self.rule(self.net.agents[agentIndex], a)
        return u

# Create the Dcontroller instance:
dcont = MyDcontroller(net=net)

# print(net.agents[0].stateTrajectHistory)
# print(net.agents[1].stateTrajectHistory)
# print(net.agents[2].stateTrajectHistory)

numOfIterations = int( (5 - 0) // 0.1 )
time_list = np.linspace(start=0, stop=5, \
                        num=numOfIterations+1, endpoint=True)
    
# %%
mas = mas.MAS(network=net, dcontroller=dcont)

mas.run(0, 15, 0.05)

mas.plotAll()
