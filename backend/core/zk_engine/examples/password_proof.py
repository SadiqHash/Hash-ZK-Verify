"""
Example: Password Verification

Prove: input password matches stored hash without revealing the password
"""

from backend.core.zk_engine.circuit_builder import CircuitBuilder


def build_circuit():
    builder = CircuitBuilder()
    circuit = builder.create_circuit("password_verification")

    circuit.add_public_input("password_hash", "hash123")
    circuit.add_private_input("password", "my_secret_password")

    circuit.add_constraint("hash(password) == password_hash")
    return circuit


def main():
    circuit = build_circuit()
    print("Verification result:", circuit.verify())


if __name__ == "__main__":
    main()
