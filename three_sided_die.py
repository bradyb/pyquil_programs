import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *

qvm = api.SyncConnection()

p = pq.Program()
p.inst(H(0)).measure(0,0)
num_flips = 3
print(qvm.run(p, [0], num_flips))