# -*- coding: utf-8 -*-
"""
Test pymas.agent.Agent class
"""

# Standard library imports


# Third party imports
import numpy as np
import matplotlib.pyplot as plt

# Local application imports
from pymas import agent

if __name__ == "__main__":
    
    def f(t, x, u):
        A = np.array([[0, 1], [-1, -2]])
        B = np.zeros(2)
        return np.dot(A, x) + np.dot(B, u)
    
    a1 = agent.Agent(f=f, t_end=5, init_states=np.array([[4], [6]]), index=1)
    steps = 100
    Ts = 0.1
    u = 0
    
    for i in range(steps+1):
        a1.evolve((i+1)*Ts, u)
     
    print(a1.stateTrajectHistory.shape)
    print(a1.times.shape)
    plt.plot(a1.times, a1.stateTrajectHistory[0, :], a1.times, a1.stateTrajectHistory[1, :])
    plt.show()
    
