# -*- coding: utf-8 -*-

"""
This is the Network class.
"""

# %% Imports
# Standard library imports
from typing import List

# Third party imports
import numpy as np

# Local application imports
from pymas.agent import Agent

# %% The distributed controller class
class Network:
    
    def __init__(self, A: np.ndarray, agents: List[Agent]):
        """
        Parameters
        ----------
        A : numpy 2D array
            This is adjacancy matrix.
        agents : List
            A list of agent objects.
        
        *** NOTE: Networks keeps the agent instances in a list so that other
        classes can access them through Network.agents. ***
        """
        self.A = A
        if len(agents) >= 2:
            self.agents = agents
        else:
            raise Exception("The number of agents should be more than one.")
        
    def areNeighbours(self, agentIndex1: int, agentIndex2: int) -> bool:
        """
        Checks if two agents are neighbours by their indices.
        NOTE: Indexing of adjacency matrix in this function is assumed to
        start from 0.
        
        *** WE SHOULD CHECK FOR NON-SYMMETRIC MATRICES, TOO. ***
        """
        if agentIndex1 != agentIndex2:
            if self.A[agentIndex1][agentIndex2] != 0:
                return True
            else:
                print(self.A[agentIndex1][agentIndex2])
                print(self.A)
        return False
        
    def get_data(self): # May be removed in future! Or not now that agents list is here!
        pass

# %% Handle direct executions
if __name__ == "__main__":
    print("network.py is not an executable module!")