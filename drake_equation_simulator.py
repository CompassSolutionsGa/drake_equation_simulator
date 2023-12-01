from qiskit import QuantumCircuit, execute, Aer
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 3 qubits
qc = QuantumCircuit(3, 3)

# Apply Hadamard gates to each qubit to create superposition states
qc.h([0, 1, 2])

# Measure the qubits
qc.measure([0, 1, 2], [0, 1, 2])

# Execute the quantum circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1024).result()
counts = result.get_counts(qc)

# Plot the results
plt.figure(figsize=(8, 6))
plt.bar(counts.keys(), counts.values())
plt.xlabel('States')
plt.ylabel('Counts')
plt.title('Probabilities of Drake Equation Factors')
plt.show()
