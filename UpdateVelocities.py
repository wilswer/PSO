#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:49:16 2019

@author: wilhelmsoderqvistwermelin
"""

import numpy as np

def UpdateVelocities(positions,velocities,particleBest,swarmBest,c1,c2,inertiaWeight,deltaTime):
    swarmSize = np.shape(velocities)[0]
    r = np.random.rand(swarmSize,1)
    q = np.random.rand(swarmSize,1)
    newVelocities = inertiaWeight*velocities + c1*q*((particleBest - positions)/deltaTime) + c2*r*((np.tile(swarmBest,[swarmSize,1]) - positions)/deltaTime)
    return newVelocities