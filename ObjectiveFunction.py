import numpy as np
from numpy import exp,sqrt,pi,cos

def ObjectiveFunction(x):
    "Defines the objective function for the problem"
    ## Himmelblau's function
    
    #if len(np.shape(x)) == 1:
    #    f = (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2;
    #else:
    #    f = (x[:,0]**2 + x[:,1] - 11)**2 + (x[:,0] + x[:,1]**2 - 7)**2;
    #return f
    
    ## Rosenbrock function
    #a = 1
    #b = 100
    #if len(np.shape(x)) == 1:
    #    f = (a - x[0])**2 + b*(x[1] - x[0]**2)**2
    #else:
    #    f = (a - x[:,0])**2 + b*(x[:,1] - x[:,0]**2)**2
    #return f
    
    ## Ackley function
    if len(np.shape(x)) == 1:
        f = -20*exp(-0.2*sqrt(0.5*(x[0]**2 + x[1]**2))) - exp(0.5*(cos(2*pi*x[0]) + cos(2*pi*x[1]))) + exp(1) + 20
    else:
        f = -20*exp(-0.2*sqrt(0.5*(x[:,0]**2 + x[:,1]**2))) - exp(0.5*(cos(2*np.pi*x[:,0]) + cos(2*pi*x[:,1]))) + exp(1) + 20
    return f
