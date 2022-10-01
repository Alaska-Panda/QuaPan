import sys
sys.path.append('../../')

import numpy as np
from core.circuit import QuCircuit


def main(args0):
	NQ_Data	    = 4
	NQ_Index	= 0 
	QC = QuCircuit(NQ_Data,NQ_Index)
	if args0 == 0:
		FLAG_GATE  = "H"
	elif args0 == 1:
		FLAG_GATE  = "X"
	elif args0 == 2:
		FLAG_GATE  = "Y"
	elif args0 == 3:
		FLAG_GATE  = "Z"

	if FLAG_GATE == "H":
		print("--H Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.cz(range(1,2+1),3)
		QC.show_OP()
		QC.add()
		print("--ALL--")
		QC.show_ALL()
		QC.tdot()
		QC.show_MAT()

	elif FLAG_GATE == "X":
		print("--X Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.cz(range(1,2+1),3)
		QC.show_OP()
		QC.add()
		print("--Operation to 2nd Quit--")
		QC.cz(range(1,2+1),3)
		QC.show_OP()
		QC.add()
		print("--ALL--")
		QC.show_ALL()
		QC.tdot()
		QC.show_MAT()

	elif FLAG_GATE == "Y":
		print("--Y Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.show_OP()
		QC.h(0)
		QC.add()
		print("--Operation to 1st Quit--")
		QC.show_OP()
		QC.cz(1,3)
		QC.add()
		print("--ALL--")
		QC.show_ALL()
		QC.tdot()
		QC.show_MAT()
		QC.show_state()

	elif FLAG_GATE == "Z":
		print("--Z Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.z(0)
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.z(1)
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.z(0)
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.z(1)
		QC.show_state()
	else:
		print("--initial state vector--")
		QC.show_state()


if __name__ == '__main__':
	args = sys.argv
	if len(args) == 2:
		if args[1].isdigit():
			main(int(args[1]))
		else: 
			print("Set the first Argument as digit")
	else:
		print("Set 1 Argument")
		print("0 -> H Gate operation")
		print("1 -> X Gate operation")
		print("2 -> Y Gate operation")
		print("3 -> Z Gate operation")
	

