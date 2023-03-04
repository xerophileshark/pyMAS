# pyMAS
A python software to simulate dynamic multi-agent systems (or networked control systems).

## Multi-Agent Systems

In simple words, multi-agent system are complex distributed systems that can be 
broken down into subsystems (agents) interacting with each other.
This interaction can be physical, such as input-output interaction between agents, or it can be 
the use of information exchanged via information and communication technology (ICT). The latter is 
in fact a subset of a larger class of systems in systems and control community called 
"networked control systems".

The interconnection topology between agents can be represented by directed graphs. The graph edges show 
the information flow between agents, while the graph nodes represent agents.

In this projects, each agent $i$ is considered as dynamical systems of the general form 

$$
\dot{x_i}(t) = f(x_i(t),u_i(t),t)
$$

where $x_i$ is the state vector, $u_i$ is the control input of agent $i$. 



## UML Class Diagram

![Class diagram](UML-class.png)

## Bibliography

