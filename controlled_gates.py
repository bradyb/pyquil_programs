import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
import numpy as np


def controlledU(u_gate):
	controlU = np.array([[1,0,0,0],
						 [0,1,0,0],
						 [0,0,u_gate[0][0],u_gate[0][1]],
						 [0,0,u_gate[1][0],u_gate[1][1]]])

	return controlU


if __name__ == "__main__":
	
	x_gate = np.array([[0,1],
						[1,0]])

	controlU = controlledU(x_gate)

	qvm = api.SyncConnection()

	p = pq.Program().defgate("CU", controlU)

	p.inst(X(1)).inst(I(0))

	wavf, _ =qvm.wavefunction(p)
	print(wavf)	

	p.inst(("CU",1,0))

	wavf, _ =qvm.wavefunction(p)
	print(wavf)
	print(controlU)

# qvm = api.SyncConnection()

# p = pq.Program()
# p.inst(H(0)).measure(0,0)
# num_flips = 3
# print(qvm.run(p, [0], num_flips))