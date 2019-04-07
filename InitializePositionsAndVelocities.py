import numpy as np

def InitializePositionsAndVelocities(numberOfParticles,numberOfVariables,xMin,xMax,alpha,deltaTime):
    "Initializes the positions and velocities of the particles"
    positions = np.zeros((numberOfParticles,numberOfVariables))
    velocities = np.zeros((numberOfParticles,numberOfVariables))
    for i in range(numberOfParticles):
        for j in range(numberOfVariables):
            r = np.random.rand()
            positions[i,j] = xMin + r*(xMax - xMin)
            velocities[i,j] = (alpha/deltaTime)*(-(xMax - xMin)/2 + r*(xMax - xMin))

    return positions,velocities
