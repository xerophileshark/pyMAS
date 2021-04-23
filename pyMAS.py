class Agent:
    currentTime = 0
    timeStep = 0.1
    initialState = []
    trajectory = []
    index = 1
    
    def __init__(self, current_time, time_step, dynamics, initial_state, index):
        self.currentTime = current_time
        self.timeStep = time_step
        self.dynamics = dynamics
        self.initialState = initial_state
        # self.trajectory.append(initial_state)
        self.index = index
    
    # The default discrete dynamics rule
    def dynamics(self):
        # The definition of agent's dynamics
        # The default dynamics would be: x(k+1) = x(k) + u_i
        pass
    
    # This function is to be used in ... class; And control_input will be fed from there
    def evolveOneStep(self, control_input)
        # return state(s) of next step
        # self.dynamics() function will be used
        # self.currentTime and self.timeStep will be used
        # self.currentTime += self.timeStep
        # self.trajectory.append(...)
        pass

class Network:
    A # Adjacancy matrix
    L # Laplacian matrix
    agents = [] # Agents
    currentAgentsStates = []
    
    def __init__(self, agents, adjacencyMatrix, distributed_controller):
        self.A = adjacencyMatrix
        self.agents = agents # A list of reference to agents objects
        self.distributedController = distributed_controller # pass by reference
        pass
    
    # The default distributed controller rule for agent i:index
    def distributedController(self, A, index):
        u_i = 0
        # u_i = {sum of ( self.agents[index].currentState - (self.currentAgentsStates in the neighbourhood) )}
        return u_i # Single Output agent
        
    def evolveOneStep(self):
        nextAgentsStates = []
        # for each agent ordered by index (i):
        #     nextAgentsStates[i] = self.agents[i].evolveOneStep(self.distributedController(self.A, i))
        # 
        # self.currentAgentsStates = nextAgentsStates

class MAS:
    N = 1
    Agents = []
    timeStep = 0.1
    A
    Network
    distributedController
    
    def __init__(self, NumOfAgents, dynamics_list, AdjacancyMatrix, time_step, distributed_controller):
        self.N = NumOfAgents
        self.Agents = []
        self.timeStep = time_step
        self.A = AdjacancyMatrix
        self.distributedController = distributed_controller
        
        for i in range(NumOfAgents):
            initialState = [0]
            self.Agents.append(Agent(0, time_step, dynamics_list[i], initialState, i))
        
        self.Network = Network(self.Agents, self.A, self.distributedController)
        
    def simulate(self, time):
        iterations = time // timeStep
        for i in iterations:
            self.Network.evolveOneStep()
    
mas = MAS(5, ...) # Create a new instance of MAS
mas.simulate(10) # Simulate for t=0 to t=10 seconds