# -*- coding: utf-8 -*-

"""
This is the MAS class.
"""

# %% Imports
# Standard library imports

# Third party imports
import numpy as np
import matplotlib.pyplot as plt

# Local application imports
from pymas.dcontroller import Dcontroller
from pymas.network import Network

# %% The multi-agent system class
class MAS:
    
    def __init__(self, network: Network, dcontroller: Dcontroller):
        """
        Parameters
        ----------
        network : Network class
            The network class instance.
        dcontroller : Dcontroller class
            The Dcontroller class instance.
        """
        self.network = network # contains agents list
        self.dcontroller = dcontroller
        
        self.init_time = None
        self.end_time = None
        self.time_step = None
        
    def run(self, init_time=0, end_time=10, time_step=0.1):
        """
        Run the simulation.
        This class currently supports homogeneous multi-agent systems.
        
        *** Do I need to use generator in the main loop of this function? ***

        Parameters
        ----------
        init_time : float, optional
            The time of the simulation start in seconds. The default is 0.
            *** Might be different from tStart in Agent class. ***
        end_time : float, optional
            Final time of simulation in seconds. The default is 10.
        time_step : float, optional
            Time step of simulation in seonds. The default is 0.1.

        Returns
        -------
        None.

        """
        # Set internal variables:
        self.init_time = init_time
        self.end_time = end_time
        self.time_step = time_step
        
        numOfIterations = int( (end_time - init_time) // time_step )
        time_list = np.linspace(start=init_time, stop=end_time, \
                                num=numOfIterations+1, endpoint=True)
        # Main for loop:
        for t in time_list[1:]:
            idx = np.where(time_list == t)
            t_prev = time_list[int(idx[0])-1]
            for agent in self.network.agents:
                agent.evolve(t, self.dcontroller.controlProtocol(agent.index, t_prev))

    # This is a temporary function for debugging
    def plot(self, agentIndex):
        plt.plot(self.network.agents[agentIndex].times, \
                 self.network.agents[agentIndex].stateTrajectHistory.\
                     reshape(len(self.network.agents[agentIndex].times), ))
        plt.grid()
        plt.show()
    
    def plotAll(self):
        for a in self.network.agents:
            plt.plot(a.times, a.stateTrajectHistory.reshape(len(a.times), ))
        plt.grid()
        plt.show()
        
# %% Handle direct executions
if __name__ == "__main__":
    print("mas.py is not an executable module!")