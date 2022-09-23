
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
		# state indextor
		self.S  = np.zeros([2,self.N],dtype=complex)
		self.S[0]  = np.ones(self.N,dtype=complex)  
		self.S = self.S.T
		self.IN  = np.diag(np.ones(self.NC,dtype=complex))
		self.OUT = np.zeros([self.NC,self.NC],dtype=complex)
		self.OP  = ["|" for i in range(self.N)]

	


	def any_base(self,index,base):
		if(type(index)==int):
			self.OP[index] = base
		elif(type(index)==range):
			L = len(index)
			for i in range(L):
				self.OP[index[i]] = base
		else:
			print("type error!")
	
	def h(self,index):
		self.any_base(index,"H")
	
	def x(self,index):
		self.any_base(index,"X")
	
	def y(self,index):
		self.any_base(index,"Y")
	
	def z(self,index):
		self.any_base(index,"Z")
	
	def show_OP(self):
		print(self.OP)
	
	def show_state(self):
		print(self.S)
		
		
