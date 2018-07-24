import math
import numpy as np
import pyquil.quil as pq
from pyquil.gates import *
from pyquil.api import QVMConnection


def single_shot_grovers(data):
	qvm = QVMConnection()
	p = pq.Program()

	data_size = int(math.log10(len(data)) / math.log10(2))
	for index in range(0,data_size):
		p.inst(H(index))

	oracle = np.identity(len(data)) - 2 * np.diag(data)
	p.defgate("oracle", oracle)
	p.inst(tuple(["oracle"] + [i for i in range(0,data_size)]))

	grover_op = 2 * (1./len(data)) * np.ones(tuple([len(data)] + [1])) * np.ones(len(data)) - np.identity(len(data))
	p.defgate("grover_op", grover_op)
	p.inst(tuple(["grover_op"] + [i for i in range(0,data_size)]))
	print(p)
	wavefunction = qvm.wavefunction(p)
	print(qvm.wavefunction(p))

single_shot_grovers([0,0,1,0])
single_shot_grovers([1,0,0,0, 0, 1, 1, 0])