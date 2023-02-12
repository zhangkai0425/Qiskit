import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, assemble, transpile

# import basic plot tools
from qiskit.visualization import plot_histogram

# Constant oracle
n = 1
# const_oracle = QuantumCircuit(n+1,n)
# output = np.random.randint(2)
# if output == 1:
#     const_oracle.x(n)

# # Balenced_oracle
# balanced_oracle = QuantumCircuit(n+1,n)

# # Controlled-NOT gates
# for qubit in range(n):
#     balanced_oracle.cx(qubit, n)
# balanced_oracle.barrier()

dj_circuit = QuantumCircuit(n+1,n)

# Apply H-gates
for qubit in range(n):
    dj_circuit.h(qubit)

# Put qubit in state |->
dj_circuit.x(n)
dj_circuit.h(n)

# Add oracle
# dj_circuit.compose(balanced_oracle)
const = False
if const == True:
    # Constant oracle
    output = np.random.randint(2)
    if output == 1:
        dj_circuit.x(n)
else:
    # Balanced_oracle
    for qubit in range(n):
        dj_circuit.cx(qubit, n)
    

# Repeat H-gates
for qubit in range(n):
    dj_circuit.h(qubit)

# Measure
for i in range(n):
    dj_circuit.measure(i,i)

# draw and save the results
dj_circuit.draw("mpl").savefig('circuit.png')

# use local simulator
aer_sim = Aer.get_backend('qasm_simulator')
shots = 1024
qobj = assemble(dj_circuit, aer_sim)
results = aer_sim.run(qobj).result()
answer = results.get_counts()

# plot and save the results
plot_histogram(answer).savefig('result.png')