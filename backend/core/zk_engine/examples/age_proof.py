"""
Example: Age Verification

Prove: user_age and age_limit without revealing user_age
"""

from backend.core.zk_engine.circuit_builder import CircuitBuilder


def build_circuit():
    builder = CircuitBuilder()
    circuit = builder.create_circuit("age_verification")

    circuit.add_public_input("age_limit", 18)
    circuit.add_private_input("user_age", 25)

    circuit.add_constraint("user_age >= age_limit")
    return circuit


def main():
    circuit = build_circuit()
    print("Verification result:", circuit.verify())


if __name__ == "__main__":
    main()
