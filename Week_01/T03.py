from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import random
from collections import Counter

shots = 1000

qc = QuantumCircuit(1, 1)
qc.h(0)            
qc.measure(0, 0)

simulator = AerSimulator()
result = simulator.run(qc, shots=shots).result()
counts = result.get_counts()

print("Quantum Counts:", counts)

quantum_bits = []

for bit, count in counts.items():
    quantum_bits.extend([int(bit)] * count)

python_bits = [random.randint(0,1) for _ in range(shots)]

python_counts = Counter(python_bits)

print("Python Counts:", python_counts)