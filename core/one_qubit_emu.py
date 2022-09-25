
import numpy as np
import math

import core.base as base

class OneQubitEmu:
	
	def __init__(self):
		self.N = 2
		# state vector
		self.S  = np.zeros([2,2],dtype=complex)
		self.S[0][0] = 1.0
		self.S[1][1] = 1.0

	def h(self):
		self.S = np.dot(base.H_GATE,self.S)
	
	def x(self):
		self.S = np.dot(base.X_GATE,self.S)
	
	def y(self):
		self.S = np.dot(base.Y_GATE,self.S)
	
	def z(self):
		self.S = np.dot(base.Z_GATE,self.S)
	
	
	def show_state(self):
		print(self.S)
		

