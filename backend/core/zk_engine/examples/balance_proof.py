"""
Example: Balance Verification

Prove: balance and required_amount without revealing balance
"""

from backend.core.zk_engine.circuit_builder import CircuitBuilder


def build_circuit():
    builder = CircuitBuilder()
    circuit = builder.create_circuit("balance_verification")

    circuit.add_public_input("required_amount", 100)
    circuit.add_private_input("balance", 500)

    circuit.add_constraint("balance >= required_amount")
    return circuit


def main():
    circuit = build_circuit()
    print("Verification result:", circuit.verify())


if __name__ == "__main__":
    main()
