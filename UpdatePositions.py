#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:17:37 2019

@author: wilhelmsoderqvistwermelin
"""

def UpdatePositions(positions,velocities,deltaTime):
    newPositions = positions + velocities*deltaTime
    return newPositions