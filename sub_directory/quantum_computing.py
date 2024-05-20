import numpy as np
arr= np.array([1,2,3])
print(arr)


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(2, 'q')
circuit = QuantumCircuit(qreg_q)

circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
# this is a test commit message
# this is the 2nd test
# this is my 3rd commit