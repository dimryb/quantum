import pkg_resources
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit.compiler import transpile
import qiskit



def print_hi(name):
    q = QuantumRegister(1)
    c = ClassicalRegister(1)
    circuit = QuantumCircuit(q, c)
    # получение состояния  |1⟩ из состояния  |0⟩
    circuit.x(q[0])
    # Применение оператора Адамара
    circuit.h(q[0])
    # Измерение состояния кубита
    circuit.measure(q, c)
    # Запуск операций на квантовом симуляторе
    result = execute(circuit, 'local qasm simulator').result()
    print(result.get_counts())


if __name__ == '__main__':
    print_hi('PyCharm')

