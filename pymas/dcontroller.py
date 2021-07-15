# -*- coding: utf-8 -*-

"""
This is the Dcontroller class.
"""

# %% Imports
# Standard library imports
from abc import ABC, abstractmethod

# Third party imports
import numpy as np

# Local application imports
from pymas.network import Network

# %% The distributed controller class
class Dcontroller(ABC):
    
    def __init__(self, net: Network):
        """
        NOTE: Agents are assumed to be homogeneous in dynamics and I/O numbers.

        """
        self.net = net
        # Initialize the outputHistory list and no (number of outputs for
        # each agent):
        self.no = self.net.agents[0].no
        
    @abstractmethod
    def rule(self, agent, neighbour):
        """
        This is the distributed control law and should be implemented.

        Parameters
        ----------
        agent : pymas.agent.Agent
            An agent instance to which the rule must be implemented.
        neighbour : pymas.agent.Agent
            A neighbour of agent.
        
        Example of implementation:
            return neighbour.stateTrajectHistory[:, -1] - agent.stateTrajectHistory[:, -1]
        """
        pass
    
    @abstractmethod
    def controlProtocol(self, agentIndex: int,  t) -> np.ndarray:
        """
        This function calculates and outputs the distributed controller's
        output for 'agentIndex'-th agent at time t to be used in the
        agent.Agent.evolve() function at time t+1.
        
        *** Note: This function could also be implemented to implement other methods 
        than average consensus control. ***
        
        Parameters
        ----------
        agentIndex : Index of the agent for which the control output should be
                calculated.
                Type: Agent class
        t : The time for calculating the control output 
                Type: float

        Returns
        -------
        The calculated output of distributed controller for agent agentIndex at time t.

        Example of implementation:
            if t == self.net.agents[agentIndex].tStart::
                latest_t = t
                return np.zeros(shape=(self.no, 1))
            if latest_t >= t:
                raise("Error: t in controlProtocol should not be repeated!")
            latest_t = t
            u = np.zeros(shape=(self.no, 1))
            for a in self.net.agents:
                if self.net.areNeighbours(a.index, agentIndex):
                    u += self.rule(self.net.agents[agentIndex], a)
            return u
        """
        pass

# %% Handle direct executions
if __name__ == "__main__":
    print("dcontroller.py is not an executable module!")