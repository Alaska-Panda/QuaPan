import sys
sys.path.append('../../')

import numpy as np
from kernel.one_qubit_emu import OneQubitEmu


def main(args0):
	QC = OneQubitEmu()
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
		QC.h()
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.h()
		QC.show_state()

	elif FLAG_GATE == "X":
		print("--X Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.x()
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.x()
		QC.show_state()

	elif FLAG_GATE == "Y":
		print("--Y Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.y()
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.y()
		QC.show_state()

	elif FLAG_GATE == "Z":
		print("--Z Gate Operation--")
		print("--init state vector--")
		QC.show_state()
		print("--Operation to 1st Quit--")
		QC.z()
		QC.show_state()
		print("--Operation to 2nd Quit--")
		QC.z()
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
		print("0 -> twice H Gate operation")
		print("1 -> twice X Gate operation")
		print("2 -> twice Y Gate operation")
		print("3 -> twice Z Gate operation")
	

