import sys
sys.path.append('../../')

import numpy as np
from kernel.base import QuCircuit


def main(args0):
	NQ_Data	    = 4
	NQ_Index	= 2 
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
		QC.h(range(1,2+1))
		QC.show_OP()
		print("--Operation to 2nd Quit--")
		QC.x(range(3,5))
		QC.show_OP()

	elif FLAG_GATE == "X":
		print("--X Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.x(0)
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.x(1)
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.x(0)
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.x(1)
		QC.show_state()

	elif FLAG_GATE == "Y":
		print("--Y Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.y(0)
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.y(1)
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.y(0)
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.y(1)
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
	

