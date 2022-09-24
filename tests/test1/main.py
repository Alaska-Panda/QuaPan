import sys
sys.path.append('../../')

import numpy as np
from kernel.one_qubit_emu import OneQubitEmu


def main():
	QC = OneQubitEmu()

	print("----")
	QC.show_state()
	print("----")
	QC.h()
	QC.show_state()
	print("----")
	QC.h()
	QC.show_state()
	print("----")
	QC.h()
	QC.show_state()
	print("----")
	QC.h()
	QC.show_state()

if __name__ == '__main__':
	main()

