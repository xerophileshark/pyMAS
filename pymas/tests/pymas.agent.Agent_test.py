# -*- coding: utf-8 -*-
"""
Test pymas.agent.Agent class
"""

###
### There is an issue in this file related to scipy.integrate:
### ValueError: too many axes: 2 (effrank=2), expected rank=1
###

# Standard library imports

# import types

# Third party imports
import numpy as np
import matplotlib.pyplot as plt

# Local application imports
import testing
from pymas import agent

if __name__ == "__main__":
    
    # define a new class which ingerits from Agent class and implements f
    class myAgent(agent.Agent):
        # Note: We "can" change the default numbers to fit our dynamics in here:
        def __init__(self, ni=1, no=1, ns=2, f=None, *, tStart=0, \
                     init_states=None, index: int=None):
            # Should call the parent's __init__ to access methods and attributes:
            # *** Pay attention to the positional and non-positional arguments. ***
            agent.Agent.__init__(self, ni, no, ns, f, tStart=tStart, \
                           init_states=init_states, index=index)
            print("Agent ", index, " has been initiated.")
                
        # A 2-state continuous and globally stable LTI dynamics for a SISO 
        # system (default Agent).
        def f(self, x, t, u):
            A = np.array([[0, 1], [-1, -2]])
            B = np.array([0, 0]).reshape(self.ns,)
            return np.dot(A, x) + np.dot(B, u)
        
        def output(self):
            return 0
    
    # Creating an agent
    a1 = myAgent(init_states=np.array([4, 6]), index=1)
    
    # Simulation
    steps = 100
    Ts = 0.1
    # u = np.zeros(shape=(a1.ni, 1))
    u = 0
    for i in range(steps+1):
        a1.evolve((i+1)*Ts, u)
        
    
    #DEBUG
    # print("DEBUG: a1.stateTrajectHistory.shape:", a1.stateTrajectHistory.shape)
    
    #Plot resulting trajectories
    # print("DEBUG: a1.times.shape:", a1.times.shape)
    plt.plot(a1.time, a1.stateTrajectHistory[:, 0], label=r"$x_1$")
    plt.plot(a1.time, a1.stateTrajectHistory[:, 1], label=r"$x_2$")
    plt.legend(title = "States")
    plt.title("Dynamics evolution of agent {}".format(a1.index))
    plt.xlabel(r"$t$")
    plt.show()
