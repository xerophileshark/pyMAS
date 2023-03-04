# -*- coding: utf-8 -*-

"""
This is the Agent class.
"""

# %% Imports
# Standard library imports
from abc import ABC, abstractmethod

# Third party imports
import numpy as np
from scipy.integrate import odeint

# Local application imports

# %% The Agent class
class Agent(ABC):
    
    def __init__(self, ni=1, no=1, ns=2, f=None, *, tStart=0, \
                 init_states=None, evolve_points=10, index: int=None):
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
        evolve_points : TYPE, optional and Keyword-only argument
            DESCRIPTION. The default is 10. Evolve points is the number of
            points in each evolve call.
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
        self.time = tStart * np.ones(shape=(1,), dtype="float")
        self.num_evolve_points = evolve_points
        if type(init_states) == np.ndarray and init_states.shape == (self.ns,):
            self.stateTrajectHistory = init_states.reshape((1, self.ns))
        else:
            print("Initial states must be like")
            self.stateTrajectHistory = np.zeros(shape=(1, self.ns))
            print(self.stateTrajectHistory)
        # Set inputTrajectory (Control input trajectory):
        self.inputTrajectory = np.zeros(shape=(self.ni,))
        
        # Agent's index
        if index != None:
            self.index = index
        else:
            raise RuntimeError("Agent's index argument should not be empty!")
            
        # # DEBUG
        # print("DEBUG: Agent {} is instantiated.".format(self.index))
    
    @abstractmethod
    def f(self, x, t, u): # -> output type
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
        *** Order of arguments is very important. ***
        x: The initial ( x(t=0) ) or previous step's ( x(t-1) ) state vector
        t: The next time step to solve ode from current time to that time.
        with appropriate dimention.
        u: The control input at time t with appropriate dimention.
        
        Returns
        -------
        The state of t+1 time step ( x(t+1) ).

        """
        A = np.random.rand(self.ns, self.ns)
        B = np.zeros(self.ns)
        return np.dot(A, x) + np.dot(B, u)

    def evolve(self, t: float, u):
        """
        This is the function that is called in each time step to evolve the
        dynamcis of the agent.

        Arguments
        ---------
        t : Next simulation time. It is passed by MAS class.
        u : Cooperative control input which is passed by Dcontroller class.
        u should be a 1-D vector and is assumed piecewise constant.
        
        Returns
        -------
        None.

        """
        
        t_list = np.linspace(self.time[-1], t, self.num_evolve_points)
        
        if self.stateTrajectHistory.ndim == 1:
            x0 = self.stateTrajectHistory[:].reshape(1, self.ns)
        else:
            x0 = self.stateTrajectHistory[-1]
            
        sol = odeint(self.f, x0.reshape((self.ns,)), t_list, args=(u,))
        
        self.time = np.append(self.time, t_list[1:], axis=0)
        self.stateTrajectHistory = np.append(self.stateTrajectHistory, \
                                             sol[1:], axis=0)
        self.inputTrajectory = np.append(self.inputTrajectory, u)
    
    @abstractmethod
    def output(self, x, u):
        """
        

        Parameters
        ----------
        x : TYPE ndarray
            The state of the system.
        u : 
            The input to the system.

        Returns
        -------
        C * self.stateTrajectHistory[-1] + D * u

        """
        C = np.array([[1, 0], [0, 1]])
        D = np.array([[0, 0], [0, 0]])
        return np.dot(C, x) + np.dot(D, u)
    
# %% Handle direct executions
if __name__ == "__main__":
    print("agent.py is not an executable module!")