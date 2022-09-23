
import numpy as np
import math


norm_H = 1./math.sqrt(2)
H_MAT = [[norm_H,norm_H],[norm_H,-norm_H]]


class QuCircuit:
	
	def __init__(self,K,M=0):
		self.K = K
		self.N = K+M
		self.M = M
		self.KC = 2**K
		self.NC = 2**self.N
		self.MC = 2**M
		#self.QM = np.zeros([self.NC,self.NC],dtype=complex)
		# state vector
		self.S  = np.zeros([2,self.N],dtype=complex)
		self.S[0]  = np.ones(self.N,dtype=complex)  
		self.S = self.S.T

	def h(self,i):
		self.S[i] = np.dot(H_MAT,self.S[i])
	
	def show_state(self):
		print(self.S)
		
		


"""
# np.tensordot(A,B,0)
def tensordot(M0,M1):
	LEN_M0 = len(M0)
	LEN_M1 = len(M1)
	LEN_A  = LEN_M0 * LEN_M1
	A = np.zeros([LEN_A,LEN_A],dtype=complex)
	for i0 in range(LEN_M0):
		for j0 in range(LEN_M0):
			for j0 in range(LEN_M1):
				for j1 in range(LEN_M1):
					A[i0*LEN_M0+i1][j0*LEN_M1+j1] = M0[i0][j0] * M1[i1][j1]
	return A
"""			

