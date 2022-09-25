
import numpy as np

from core.circuit import QuCircuit


def input_zeros(K,M=0):
	N =K+M
	NN = 2 ** N
	S  = np.zeros(NN,dtype=complex)
	S[0]  = 1.0  
	#S = S.T
	return S

def input_h(K,M=0):
	QC = QuCircuit(K,M)
	QC.h(range(0,K+M))
	QC.add()
	QC.tdot()
	A = QC.rt_QMatrix()
	return A[0]


