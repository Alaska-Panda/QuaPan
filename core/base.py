
import math
import numpy as np

norm_H = 1./math.sqrt(2)

H_GATE = [[norm_H,norm_H],[norm_H,-norm_H]]
I_GATE = [[1.0,0],[0,1.0]]
X_GATE = [[0,1.0],[1.0,0]]
Y_GATE = [[0,-1.0j],[1.0j,0]]
Z_GATE = [[1.0,0],[0,-1.0]]
C0_MAT = [[1.0,0],[0,0]]
C1_MAT = [[0,0],[0,1.0]]

