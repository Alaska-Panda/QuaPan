
import core.base as base
import numpy as np

def trans_mat(A):
	if A == "-":
		B = base.I_GATE
	elif A == "H":
		B = base.H_GATE
	elif A == "X":
		B = base.X_GATE
	elif A == "Y":
		B = base.Y_GATE
	elif A == "Z":
		B = base.Z_GATE
	elif A == "*":
		B = base.C1_MAT
	else:
		B = base.I_GATE
	return B


def sub_tensor(A):
	L = len(A)
	#print(A)
	for i in range(L):
		if i == 0:
			MAT  = trans_mat(A[i])
		else:
			#MAT = np.tensordot(trans_mat(A[i]),MAT,axes=0)
			MM = trans_mat(A[i])
			L0 = 2**i
			M0 = np.zeros([L0*2,L0*2],dtype=complex)
			for k0 in range(L0):
				for k1 in range(L0):
					for j0 in range(2):
						for j1 in range(2):
							M0[k0*2+j0][k1*2+j1] = MAT[k0][k1] * MM[j0][j1]
			MAT = M0
	return MAT	


# to add a pass control matrix 
def sub_ctrl(MAT):
	L = len(MAT)
	for i in range(L):
		if np.sum(np.abs(MAT[i])) == 0.0:
			MAT[i][i] = 1.0

	return MAT	
"""
def sub_ctrl(A,MAT):
	L = len(A)
	#print(A)
	index = 0
	for i in range(L):
		if A[i] == "*":
			L0 = 2**i
			MAT[L0][L0]     = 1.0
			MAT[L0+1][L0+1] = 1.0
	return MAT
"""

def tensor(N,A,CTRL,TARGET):
	L = len(A)
	#B = np.zeros([N,N],dtype=complex)
	for i in range(L):
		if i == 0:
			if CTRL[i] == 0:
				B = sub_tensor(A[i])
			else:
				B0 = sub_tensor(A[i])
				B = sub_ctrl(B0)
		else:
			if CTRL[i] == 0:
				C = sub_tensor(A[i])
			else:
				C0 = sub_tensor(A[i])
				C = sub_ctrl(C0)
			B = np.dot(B,C)
	return B


