import sys
sys.path.append('../')

import numpy as np
import matplotlib.pyplot as plt
from core.circuit import QuCircuit
from core.input import *

FLAG_DEBUG = 1 

def oracle(QC,NQubits,PATTERN):
	mask = (1<<NQubits) - 1
	A = PATTERN ^ mask
	for i in range(NQubits):
		if ((A >> (NQubits - i -1))  & 1):
			QC.x(i)


def main(args0,args1,args2):
	NQ_Data	    = args0
	NQ_Index	= 0 
	NQ_ALL      = NQ_Data + NQ_Index
	N_DATA_SET  = 1<<NQ_ALL
	NUM_ITR     = int(np.pi /4.0 * np.sqrt(N_DATA_SET/1.0))
	#print(np.pi /4.0 * (NQ_ALL/1.0))
	print("NUMBER OF ITERATIONS :", NUM_ITR)  
	#QC_INPUT  = input_zeros(NQ_Data,NQ_Index)
	QC_INPUT  = input_h(NQ_Data,NQ_Index)
	if FLAG_DEBUG==1:
		print(QC_INPUT)
		print(input_zeros(NQ_Data,NQ_Index))
	
	QC = QuCircuit(NQ_Data,NQ_Index)
	
	SEARCH_PATTERN = args1
	
	if args2 == 1:
		FLAG_SIM = "ON"
	else:
		FLAG_SIM = "OFF"

	for i in range(NUM_ITR):
		# Oracle
		print("Oracle x",i+1,":Diffuser x",i)
		oracle(QC,NQ_ALL,SEARCH_PATTERN)
		QC.add()
		QC.cz(range(0,NQ_ALL-1),NQ_ALL-1)
		QC.add()
		oracle(QC,NQ_ALL,SEARCH_PATTERN)
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
		QC.show_ALL()

	if FLAG_SIM == "ON":
		QC.tdot()
		if FLAG_DEBUG == 1:
			QC.show_MAT()
		print("--Simulation--")
		GROVER_MAT = QC.rt_QMatrix()
		QC_OUT = np.dot(GROVER_MAT,QC_INPUT)
		#OUTPUT = (QC_OUT)
		PROB_ANSWER = np.square(QC_OUT).real*100.0
		print("--Probabilities in Simulation--")
		for i in range(0,N_DATA_SET):
			print("#",i,":",format(PROB_ANSWER[i],"3.1f"),"[%]")
		print("Estimated Answer :", np.argmax(PROB_ANSWER))
		print('Probability of Answer [%] :',format(PROB_ANSWER[np.argmax(PROB_ANSWER)],"3.1f"))
		x = [i for i in range(0,N_DATA_SET)]
		y = PROB_ANSWER
		plt.bar(x,y)
		plt.xlabel("Searched Number")
		plt.ylabel("Probability [%]")
		plt.xlim(0,N_DATA_SET-1)
		plt.ylim(0.0,100.0)
		plt.show()
	else:
		print("Skip Simulation")
	


if __name__ == '__main__':
	args = sys.argv
	if len(args) == 4:
		if args[1].isdigit() & args[2].isdigit() & args[3].isdigit():
			main(int(args[1]),int(args[2]),int(args[3]))
		else: 
			print("Set  Arguments as int")
	else:
		print("Set 3 Arguments")
		print("#1 : Number of Qubits")
		print("#2 : Search DB Pattern")
		print("#3 : Simulation OFF, ONF = {0,1}")
		print("example: python3 auto_grover_v1.py 4 7 1")
	

