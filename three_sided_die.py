import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *

qvm = api.QVMConnection()

p = pq.Program()
p.inst(H(0)).measure(0,0)
num_flips = 3
results = qvm.run(p, [0], num_flips)
print(results)

roll = 0
for trial in range(0,num_flips):
	roll = roll + 2**trial * results[trial][0]

print(roll)
