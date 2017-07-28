import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
import numpy as np
import math


##
## Returned operator is defined to be
## the operator that rotates a quibit 
## by theta around the r_vec axis. This is
## cos(theta/2) * I - i*sin(theta/2)(r_vec \cdot (X,Y,Z))
## where X,Y,Z are the Pauli operators
##

def rotation_operator(r_vec, theta):

	x_gate = np.array([[0,1],
						[1,0]])

	y_gate = np.array([[0,-1j],
						[1j,0]])

	z_gate = np.array([[1,0],
						[0,-1]])

	i_gate = np.array([[1,0],
						[0,1]])

	return ( math.cos(theta / 2.0) * i_gate - 1j * math.sin(theta/2) * 
						(r_vec[0] * x_gate + r_vec[1] * y_gate + r_vec[2] * z_gate))


## Write Function that returns CZ, has this been done by Rigetti???

if __name__ == "__main__":
	print (rotation_operator([1,0,0],math.pi)==np.array([[0,-1j],[-1j,0]]))
	print (rotation_operator([0,1,0],math.pi)==np.array([[0,-1],[1,0]]))
	print (rotation_operator([0,0,1],math.pi)==np.array([[-1j,0],[0,1j]]))

