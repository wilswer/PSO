import numpy as np
from ObjectiveFunction import ObjectiveFunction

def EvaluateSwarm(positions):
    "Evaluates the swarm"
    swarmFunctionValues = ObjectiveFunction(positions)
    return swarmFunctionValues
