from qiskit import QuantumCircuit, execute, Aer
import matplotlib.pyplot as plt
import numpy as np

# Create a Quantum Circuit with 1 qubit
qc = QuantumCircuit(1, 1)

# Apply a Hadamard gate to put the qubit in superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Execute the quantum circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1).result()
counts = result.get_counts(qc)

# Extract a random number (0 or 1) from the measurement
random_bit = int(list(counts.keys())[0])

# Drake Equation Factors (with one factor modified by the quantum result)
factors = {
    'R_star': 1.5,       # Average rate of star formation per year in our galaxy
    'f_p': 0.5,          # Fraction of those stars that have planetary systems
    'n_e': 2,            # Average number of planets that could potentially support life per star with planets
    'f_l': 1,            # Fraction of planets that could support life where life actually appears
    'f_i': 0.1 + 0.05 * random_bit,  # Fraction of planets with life that develop intelligent life (modified by quantum result)
    'f_c': 0.1,          # Fraction of civilizations that develop a technology to release detectable signs of their existence
    'L': 10000           # Length of time such civilizations release detectable signals (years)
}

# Calculate N, the number of detectable civilizations in our galaxy
N = np.prod(list(factors.values()))

# Print the result
print(f"The estimated number of detectable civilizations in our galaxy is: {N}")

# Plot the factors
plt.figure(figsize=(10, 6))
plt.bar(factors.keys(), factors.values(), color='skyblue')
plt.xlabel('Factors')
plt.ylabel('Values')
plt.title('Factors of the Drake Equation Modified by Quantum Computation')
plt.yscale('log') # Using logarithmic scale due to wide range of values
plt.show()