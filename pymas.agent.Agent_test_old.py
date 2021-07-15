# -*- coding: utf-8 -*-
"""
Test pymas.agent.Agent class
"""

# Standard library imports
# import types

# Third party imports
import numpy as np
import matplotlib.pyplot as plt

# Local application imports
from pymas import agent
# from pymas.utils.addmethod import add_method

if __name__ == "__main__":
    
    # A 2-state continuous and globally stable LTI dynamics for a SISO system.
    def f(t, x, u):
        A = np.array([[0, 1], [-1, -2]])
        B = np.zeros(2)
        return np.dot(A, x) + np.dot(B, u)
    
    # Creating an agent
    a1 = agent.Agent(f=f, t_end=5, init_states=np.array([[4], [6]]), index=1)
    
    # a1 = agent.Agent(t_end=5, init_states=np.array([[4], [6]]), index=1)
    # Decorator can be written to take normal functions and make them methods
    # @add_method(a1)
    # def f(t, x, u):
    #     A = np.array([[0, 1], [-1, -2]])
    #     B = np.zeros(2)
    #     return np.dot(A, x) + np.dot(B, u)
    
    # Using types module to append f to a1:
    # a1.f = types.MethodType(f, a1)
    
    # Simulation
    steps = 100
    Ts = 0.1
    u = 0
    for i in range(steps+1):
        a1.evolve((i+1)*Ts, u)
    
    #DEBUG
    print("DEBUG: a1.stateTrajectHistory.shape:", a1.stateTrajectHistory.shape)
    
    #Plot resulting trajectories
    print(a1.times.shape)
    plt.plot(a1.times, a1.stateTrajectHistory[0, :], label=r"$x_1$")
    plt.plot(a1.times, a1.stateTrajectHistory[1, :], label=r"$x_2$")
    plt.legend(title = "States")
    plt.title("Dynamics evolution of agent {}".format(a1.index))
    plt.xlabel(r"$t$")
    plt.show()
