import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *

qvm = api.SyncConnection()

p = pq.Program()