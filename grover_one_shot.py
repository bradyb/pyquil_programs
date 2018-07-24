import math
import pyquil.quil as pq
from pyquil.gates import *
from pyquil.api import QVMConnection


def single_shot_grovers(data):
	qvm = QVMConnection()
	p = pq.Program()

	data_size = int(math.log10(len(data)) / math.log10(2))
	for index in range(0,data_size):
		p.inst(H(index))

	print(p)
	wavefunction = qvm.wavefunction(p)
	print(qvm.wavefunction(p))

single_shot_grovers([1,0,0,0])