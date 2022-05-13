import pkg_resources
from qiskit import Aer


# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')