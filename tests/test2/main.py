import sys
sys.path.append('../../')

import numpy as np
from kernel.circuit import QuCircuit


def main():
	NQ_Data	= 2
	NQ_Index	= 0 
	QC = QuCircuit(NQ_Data,NQ_Index)

	print("----")
	QC.show_state()
	print("----")
	QC.h(0)
	QC.show_state()
	print("----")
	QC.h(1)
	QC.show_state()
	print("----")
	QC.h(0)
	QC.show_state()
	print("----")
	QC.h(1)
	QC.show_state()

if __name__ == '__main__':
	main()

