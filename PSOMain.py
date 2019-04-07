import numpy as np
import matplotlib.pyplot as plt
from InitializePositionsAndVelocities import InitializePositionsAndVelocities
from EvaluateSwarm import EvaluateSwarm
from UpdateVelocities import UpdateVelocities
from UpdatePositions import UpdatePositions
from ObjectiveFunction import ObjectiveFunction
from mpl_toolkits.mplot3d import Axes3D


numberOfParticles = 30
numberOfVariables = 2
inertiaWeight = 1.4
inertiaWeightDecrease = 0.999
alpha = 1
deltaTime = 1
xMin = -5
xMax = 5
maxIteration = 100
maxVelocity = 10;
c1 = 2;
c2 = 2;

[positions,velocities] = InitializePositionsAndVelocities(numberOfParticles,numberOfVariables,xMin,xMax,alpha,deltaTime)
swarmFunctionValues = np.empty([1, numberOfParticles])

jFig = 0

YNplot = int(input('Plot swarm? Yes (1) or No (0): '))

for i in range(maxIteration):
    if i == 0:
        swarmFunctionValues = EvaluateSwarm(positions)
        particleBestIndex = np.arange(numberOfParticles)
        particleBest = positions[particleBestIndex,:]
        swarmBestIndex = np.argmin(swarmFunctionValues)
        swarmBest = positions[swarmBestIndex,:]
    else:
        swarmFunctionValues = np.vstack((swarmFunctionValues,EvaluateSwarm(positions)))
        swarmBestIndex = np.argwhere(swarmFunctionValues == np.min(swarmFunctionValues))[0,:]
        if swarmBestIndex[0] == i:
            swarmBest = positions[swarmBestIndex[1],:]
        particleBestIndex = swarmFunctionValues == np.amin(swarmFunctionValues,axis = 0)
        particleBestIndex = 1*particleBestIndex[-1,:].T;
        particleBest = particleBest.T*(1-particleBestIndex) + positions.T*(particleBestIndex)
        particleBest = particleBest.T
    if inertiaWeight > 0.4:
        inertiaWeight = inertiaWeightDecrease*inertiaWeight    
    if YNplot == 1 and i%10 == 0:
        fig = plt.figure(0)
        ax = fig.add_subplot(111, projection='3d')
        x = y = np.arange(-20.0, 20.0, 0.05)
        X, Y = np.meshgrid(x, y)
        XY = np.array([np.ravel(X), np.ravel(Y)]).T
        zs = np.array(ObjectiveFunction(XY))
        Z = zs.reshape(X.shape)
        
        ax.plot_surface(X, Y, Z)
        ax.scatter(positions[:,0],positions[:,1],ObjectiveFunction(positions),color = "k",s=100,alpha = 1)
        ax.scatter(swarmBest[0],swarmBest[1],ObjectiveFunction(swarmBest),color = "r",s=100,alpha = 1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('f(X,Y)')
        plt.pause(0.05)
    
    velocities = UpdateVelocities(positions,velocities,particleBest,swarmBest,c1,c2,inertiaWeight,deltaTime)
    velocities[velocities > maxVelocity] = maxVelocity
    velocities[velocities < -maxVelocity] = -maxVelocity
    positions = UpdatePositions(positions,velocities,deltaTime);

print('Best function value: ' + str(ObjectiveFunction(swarmBest)) + ' at x = ' + str(swarmBest))

fig = plt.figure(0)
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-20.0, 20.0, 0.05)
X, Y = np.meshgrid(x, y)
XY = np.array([np.ravel(X), np.ravel(Y)]).T
zs = np.array(ObjectiveFunction(XY))
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)
ax.scatter(swarmBest[0],swarmBest[1],ObjectiveFunction(swarmBest),color = "r",s=100,alpha = 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X,Y)')

plt.tight_layout()
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)
plt.show()