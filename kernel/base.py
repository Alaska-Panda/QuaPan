
import math
import numpy as np

norm_H = 1./math.sqrt(2)
"""
H_GATE = np.zeros([2,2],dtype=complex)
I_GATE = np.zeros([2,2],dtype=complex)
X_GATE = np.zeros([2,2],dtype=complex)
Y_GATE = np.zeros([2,2],dtype=complex)
Z_GATE = np.zeros([2,2],dtype=complex)
H_GATE[0][0] =  norm_H
H_GATE[0][1] =  norm_H
H_GATE[1][0] =  norm_H
H_GATE[1][1] = -norm_H


I_GATE[0][0] = 1.0
I_GATE[1][1] = 1.0
X_GATE[0][1] = 1.0
X_GATE[1][0] = 1.0
Y_GATE[0][1] = -1.0j
Y_GATE[1][0] = 1.0j
X_GATE[0][0] = 1.0
X_GATE[1][1] = -1.0

"""
H_GATE = [[norm_H,norm_H],[norm_H,-norm_H]]
I_GATE = [[1.0,0],[0,1.0]]
X_GATE = [[0,1.0],[1.0,0]]
Y_GATE = [[0,-1.0j],[1.0j,0]]
Z_GATE = [[1.0,0],[0,-1.0]]

