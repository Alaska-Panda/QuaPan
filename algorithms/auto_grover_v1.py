import sys
sys.path.append('../')

import numpy as np

from core.circuit import QuCircuit
from core.input import *

def oracle(QC,NQubits,PATTERN):
	mask = (1<<NQubits) - 1
	A = PATTERN ^ mask
	for i in range(NQubits):
		if ((A >> (NQubits - i -1))  & 1):
		#if ((A >> i)  & 1):
			QC.x(i)


def main(args0,args1,args2):
	NQ_Data	    = args0
	NQ_Index	= 0 
	NQ_ALL      = NQ_Data + NQ_Index
	NUM_ITR     = int(np.pi /4.0 * (NQ_ALL/1.0))
	#print(np.pi /4.0 * (NQ_ALL/1.0))
	print("NUMBER OF ITERATIONS :", NUM_ITR)  
	#QC_INPUT  = input_zeros(NQ_Data,NQ_Index)
	QC_INPUT  = input_h(NQ_Data,NQ_Index)
	print(QC_INPUT)
	print(input_zeros(NQ_Data,NQ_Index))
	
	QC = QuCircuit(NQ_Data,NQ_Index)
	
	SEARCH_PATTERN = args1
	
	if args2 == 1:
		FLAG_SIM = "ON"
	else:
		FLAG_SIM = "OFF"

	if SEARCH_PATTERN == "0":
		print("--Answer : 000--")
	elif SEARCH_PATTERN == "1":
		print("--Answer : 001--")
	elif SEARCH_PATTERN == "2":
		print("--Answer : 010--")
	elif SEARCH_PATTERN == "3":
		print("--Answer : 011--")
	elif SEARCH_PATTERN == "4":
		print("--Answer : 100--")
	elif SEARCH_PATTERN == "5":
		print("--Answer : 101--")
	elif SEARCH_PATTERN == "6":
		print("--Answer : 110--")
	elif SEARCH_PATTERN == "7":
		print("--Answer : 111--")
	else:
		print("--Answer : 000--")

	for i in range(NUM_ITR):
		# Oracle
		print("Oracle x",i+1,":Diffuser x",i)
		oracle(QC,NQ_ALL,SEARCH_PATTERN)
		QC.add()
		QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
		QC.add()
		oracle(QC,NQ_ALL,SEARCH_PATTERN)
		QC.add()
		"""
		if SEARCH_PATTERN == 0:
			QC.x(range(0,NQ_ALL))
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(range(0,NQ_ALL))
			QC.add()
		elif SEARCH_PATTERN == 1:
			QC.x(range(0,2))
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(range(0,2))
			QC.add()
		elif SEARCH_PATTERN == 2:
			QC.x(0)
			QC.x(2)
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(0)
			QC.x(2)
			QC.add()
		elif SEARCH_PATTERN == 3:
			QC.x(0)
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(0)
			QC.add()
		elif SEARCH_PATTERN == 4:
			QC.x(range(1,3))
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(range(1,3))
			QC.add()
		elif SEARCH_PATTERN == 5:
			QC.x(1)
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(1)
			QC.add()
		elif SEARCH_PATTERN == 6:
			QC.x(2)
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(2)
			QC.add()
		elif SEARCH_PATTERN == 7:
			#QC.x(range(0,2))
			#QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			#QC.add()
			#QC.x(range(0,2))
			QC.add()
		else: # SEARCH_PATTERN == 0
			QC.x(range(0,NQ_ALL))
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(range(0,NQ_ALL))
			QC.add()
		"""
		QC.show_ALL()
		# Diffuser
		print("Oracle x",i+1,":Diffuser x",i+1)
		QC.h(range(0,NQ_ALL))
		QC.add()
		QC.x(range(0,NQ_ALL))
		QC.add()
		QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
		QC.add()
		QC.x(range(0,NQ_ALL))
		QC.add()
		QC.h(range(0,NQ_ALL))
		QC.add()
	#QC.h(range(0,NQ_ALL))
	#QC.add()

	if FLAG_SIM == "ON":
		QC.tdot()
		QC.show_MAT()
		print("--Simulation--")
		GROVER_MAT = QC.rt_QMatrix()
		QC_OUT = np.dot(GROVER_MAT,QC_INPUT)
		#OUTPUT = (QC_OUT)
		PROB_ANSWER = np.square(QC_OUT)
		print("--Probability of Output as Answer--")
		print(PROB_ANSWER)
		print("Estimated Answer :", np.argmax(PROB_ANSWER))
	else:
		print("Skip Simulation")
	


if __name__ == '__main__':
	args = sys.argv
	if len(args) == 4:
		if args[1].isdigit() & args[2].isdigit() & args[3].isdigit():
			main(int(args[1]),int(args[2]),int(args[3]))
		else: 
			print("Set the first Argument as digit")
	else:
		print("Set 1 Argument")
		print("0 -> H Gate operation")
		print("1 -> X Gate operation")
		print("2 -> Y Gate operation")
		print("3 -> Z Gate operation")
	

