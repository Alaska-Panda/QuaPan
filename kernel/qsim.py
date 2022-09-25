
import numpy as np
import math

from kernel.tensor import tensor
import kernel.base as base


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
		self.CTRL = []
		self.CTRL_BIT = 0
		#self.OP  = ["|" for i in range(self.N)]
		self.init_OP()
		self.MatrixOP  = []

	def init_OP(self):
		self.OP  = ["-" for i in range(self.N)]
		self.CTRL_BIT = 0
		self.CTRL_TARGET = "-" 

	def any_base(self,index,base):
		self.CTRL_BIT = 0
		if(type(index)==int):
			self.OP[index] = base
		elif(type(index)==range):
			L = len(index)
			for i in range(L):
				self.OP[index[i]] = base
		else:
			print("type error!")

	def any_ctrl(self,index,target,base):
		self.CTRL_BIT =  1
		self.CTRL_TARGET =  target
		if(type(index)==int):
			self.OP[index] = "*"
			self.OP[target] = base
		elif(type(index)==range):
			L = len(index)
			for i in range(L):
				self.OP[index[i]] = "*" 
			self.OP[target] = base
		elif(type(index)==list):
			L = len(index)
			for i in range(L):
				self.OP[index[i]] = "*" 
			self.OP[target] = base
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
	
	def cx(self,index,target):
		self.any_ctrl(index,target,"X")
	
	def cy(self,index,target):
		self.any_ctrl(index,target,"Y")
	
	def cz(self,index,target):
		self.any_ctrl(index,target,"Z")
	
	
	def add(self):
		self.MatrixOP.append(self.OP)
		self.CTRL.append(self.CTRL_BIT)
		self.init_OP()
	
	def tdot(self):
		self.MAT = tensor(self.NC,self.MatrixOP,self.CTRL,self.CTRL_TARGET)
	
	def show_OP(self):
		print(self.OP)
	

	def show_ALL(self):
		
		L = len(self.MatrixOP)
		K = len(self.MatrixOP[0])
		print("matrix size : ",L,"x",K)
		for k in range(K):
			A = []
			for i in range(L):
				A.append(self.MatrixOP[i][k])
			print(A)	
	
	def show_MAT(self):
		for i in range(self.NC):
			#for k in range(self.NC):
			print(self.MAT[i])
		#print(self.MAT)
	
	def show_state(self):
		print(self.S)
		
		
