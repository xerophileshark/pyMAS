# pyMAS

A python package to simulate dynamic multi-agent systems (or networked control systems).
This package is designed to help research the effects of faults and cyber-attacks on a MAS.

## Multi-Agent Systems

In simple words, multi-agent system (MAS) are complex distributed systems that can be 
broken down into subsystems (agents) interacting with each other.
This interaction can be physical, such as input-output interaction between agents, or it can be 
the use of information exchanged via information and communication technology (ICT). The latter is 
in fact a subset of a larger class of systems in systems and control community called 
"networked control systems".

The interconnection topology between agents can be represented by directed graphs. The graph edges show 
the information flow between agents, while the graph nodes represent agents.

In this projects, each agent $i$ is considered as continuous-time dynamical systems of the general form 

$$
\dot{x}_i(t) = f(x_i(t),u_i(t),t)
$$

where $x_i(t)$ is the state vector, $u_i(t)$ is the control input of agent $i$. The control input 
can be designed in a distributed way using the information received from the neighboring agents of 
the agent $i$.

### Consensus in MASs

The consensus in MASs is reffered to the problem where it is desired for all agents to reach at the same 
value for some variables (states) at some point in time. As an example, in a homogenous MAS of $n$ agents 
of order one (integrator agents), i.e.,

$$
\dot{x}_i(t) = u_i(t)
$$

the following control law can solve the consensus problem. For more information on MAS and consensus on graphs, 
please reffer to [1] and references therein.

$$
u_i(t) = \sum_{j\in \mathcal{N}_i}^{} \big(x_j(t) - x_i(t)\big)
$$

where \mathcal{N}_i is the set of agent $i$'s neighboring agents.

## UML Class Diagram

![Class diagram](UML-class.png)

## Bibliography

[1] 
[2] 