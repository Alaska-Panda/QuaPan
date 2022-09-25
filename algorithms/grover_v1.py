import sys
sys.path.append('../')

import numpy as np

from core.circuit import QuCircuit
from core.input import *

def main(args0,args1):
	NQ_Data	    = 3
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
	if args0 == 0:
		FLAG_GATE  = "0"
	elif args0 == 1:
		FLAG_GATE  = "1"
	elif args0 == 2:
		FLAG_GATE  = "2"
	elif args0 == 3:
		FLAG_GATE  = "3"
	
	if args1 == 1:
		FLAG_SIM = "ON"
	else:
		FLAG_SIM = "OFF"

	if FLAG_GATE == "0":
		print("--Answer : 000--")
	elif FLAG_GATE == "1":
		print("--Answer : 001--")
	for i in range(NUM_ITR):
		# Oracle
		if FLAG_GATE == "0":
			print("Oracle x",i+1,":Diffuser x",i)
			QC.x(range(0,NQ_ALL))
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(range(0,NQ_ALL))
			QC.add()
			QC.show_ALL()
		elif FLAG_GATE == "1":
			print("Oracle x",i+1,":Diffuser x",i)
			QC.x(range(0,2))
			QC.add()
			QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
			QC.add()
			QC.x(range(0,2))
			QC.add()
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
	if len(args) == 3:
		if args[1].isdigit():
			main(int(args[1]),int(args[2]))
		else: 
			print("Set the first Argument as digit")
	else:
		print("Set 1 Argument")
		print("0 -> H Gate operation")
		print("1 -> X Gate operation")
		print("2 -> Y Gate operation")
		print("3 -> Z Gate operation")
	

