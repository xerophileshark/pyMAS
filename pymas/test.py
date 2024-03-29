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
import agent

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
        
        # A 2-state continuous and globally stable LTI dynamics for a SISO 
        # system (default Agent).
        def f(self, t, x, u):
            return u
    
    # Creating an agent
    init_states = np.array([[4], [6]])
    a1 = myAgent(ni=1, no=1, ns=2, tStart=0, \
                                 init_states=init_states, index=1)
    
    # Simulation
    end_time = 5
    init_time = 0
    time_step = 0.1
    numOfIterations = int( (end_time - init_time) // time_step )
    time_list = np.linspace(start=init_time, stop=end_time, \
                                num=numOfIterations+1, endpoint=True)
    # Main for loop:
    for t in time_list[1:]:
        u = np.zeros(shape=(a1.ni, 1))
        idx = np.where(time_list == t)
        t_prev = time_list[int(idx[0])-1]
        a1.evolve(t, u)
        
