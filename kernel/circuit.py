
import numpy as np
import math


norm_H = 1./math.sqrt(2)
H_GATE = [[norm_H,norm_H],[norm_H,-norm_H]]
X_GATE = [[0,1.0],[1.0,0]]
Y_GATE = [[0,-1.0j],[1.0j,0]]
Z_GATE = [[1.0,0],[0,-1.0]]


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
		self.S[i] = np.dot(H_GATE,self.S[i])
	
	def x(self,i):
		self.S[i] = np.dot(X_GATE,self.S[i])
	
	def y(self,i):
		self.S[i] = np.dot(Y_GATE,self.S[i])
	
	def z(self,i):
		self.S[i] = np.dot(Z_GATE,self.S[i])
	
	def cz(self,vec,n):
		L = len(vec)
		norm = complex(1.0)
		for i in range(L):
			norm = norm * S[vec[i]][1] 
		if(norm == 1.0):
			self.S[i] = np.dot(Z_GATE,self.S[i])
			
	
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

