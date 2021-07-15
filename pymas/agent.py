# -*- coding: utf-8 -*-

"""
This is the Agent class.
"""

# %% Imports
# Standard library imports
from abc import ABC, abstractmethod

# Third party imports
import numpy as np
from scipy.integrate import ode

# Local application imports

# %% The Agent class
class Agent(ABC):
    
    def __init__(self, ni=1, no=1, ns=2, f=None, *, tStart=0, \
                 init_states=None, index: int=None):
        """
        Parameters
        ----------
        ni : TYPE, optional
            DESCRIPTION. Number of inputs. The default is 1.
        no : TYPE, optional
            DESCRIPTION. Number of outputs. The default is 1.
            *** This output is sent through communication network.
        ns : TYPE, optional
            DESCRIPTION. Number of states. The default is 2.
        f : TYPE, optional
            DESCRIPTION. The dynamics function.
            The default is a simple double-integrator.
        tStart: float, optional
            *** It is always 0 except when an agent is introduced to the MAS 
            in the middle of simulation.
        init_states : TYPE, optional and Keyword-only argument
            DESCRIPTION. The initial values for states. The default is
            the zero vector.
        index : TYPE, optional and Keyword-only argument
            DESCRIPTION. The default is None. But it should be set in higher
            level classes.

        Returns
        -------
        None.

        """
        # Override the default function self.f() if f is provided
        if f != None:
            self.f = f
        self.ni = ni
        self.no = no
        self.ns = ns
        
        # Set simulation parameters and initial states (time is in seconds)
        self.tStart = tStart # tStart is always 0
        self.times = np.zeros(shape=(1,), dtype="float")
        if type(init_states) == np.ndarray and init_states.shape == (self.ns, 1):
            self.stateTrajectHistory = init_states
        else:
            self.stateTrajectHistory = np.zeros(shape=(self.ns, 1))
        # Set inputTrajectory (Control input trajectory):
        self.inputTrajectory = np.zeros(shape=(self.ni, 1))
        
        # Set the ODE solver
        self.r = ode(self.f).set_integrator("dopri5") # *** PASS BY REFRENCE??
        self.r.set_initial_value(self.stateTrajectHistory[:, 0], self.tStart)        
        
        # Agent's index
        if index != None:
            self.index = index
        else:
            raise RuntimeError("Agent's index argument should not be empty!")
            
        # # DEBUG
        # print("DEBUG: Agent {} is instantiated.".format(self.index))
    
    @abstractmethod
    def f(self, t, x, u): # -> output type
        """
        This is the default function in dynamics equation of the agent
        in the form of state ODE equations:
            dx/dt = f(t, x(t), u(t))
        where x is the state vector. In this default form
            f(x, u) = A*x + B*u.
        This function is used in ode class and should be like:
            f(t, x, *args)
        which *args here is u and is set via set_f_params() function
        
        Arguments
        ---------
        t: The next time step to solve ode from current time to that time.
        x: The initial ( x(t=0) ) or previous step's ( x(t-1) ) state vector
        with appropriate dimention.
        u: The control input at time t with appropriate dimention.
        
        Returns
        -------
        The state of t+1 time step ( x(t+1) ).

        """
        A = np.random.rand(self.ns, self.ns)
        B = np.zeros(self.ns)
        return np.dot(A, x) + np.dot(B, u)
    
    # def evolve(self, t, u):
    #     """
    #     This is the function that is called in each time step to evolve the
    #     dynamcis of the agent.

    #     Arguments
    #     ---------
    #     t: Next simulation time. It is passed by MAS class.
    #     --> ***: in repeated calls, t should be increased.
    #     u: Cooperative control input which is passed by MAS and Network
    #     classes.--> *** NOTE: This may change!
        
    #     Returns
    #     -------
    #     None.

    #     """
    #     self.r.set_f_params(u)
    #     res = self.r.integrate(t)
    #     if not self.r.successful():
    #         raise RuntimeError("Agent.agent.evolve(): Could not integrate")
    #     self.times = np.append(self.times, t)
    #     self.stateTrajectHistory = np.append(self.stateTrajectHistory, res.reshape((self.ns, 1)), axis=1)

    def evolve(self, t: float, u):
        """
        This is the function that is called in each time step to evolve the
        dynamcis of the agent.

        Arguments
        ---------
        t : Next simulation time. It is passed by MAS class.
        u : Cooperative control input which is passed by Dcontroller class.
        
        Returns
        -------
        None.

        """
        self.r.set_f_params(u) # set the control input at current time ( u(t0) ).
        res = self.r.integrate(t)
        if not self.r.successful():
            raise RuntimeError("Agent.agent.evolve(): Could not integrate")
        self.times = np.append(self.times, t)
        self.stateTrajectHistory = np.append(self.stateTrajectHistory, \
                                             res.reshape((self.ns, 1)), axis=1)
        self.inputTrajectory = np.append(self.inputTrajectory, u, axis=1)
        
# %% Handle direct executions
if __name__ == "__main__":
    print("agent.py is not an executable module!")