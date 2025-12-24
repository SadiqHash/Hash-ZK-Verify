from backend.core.zk_engine.circuit_builder import CircuitBuilder
from backend.core.zk_engine.proof_generator import ProofGenerator
from backend.core.zk_engine.verifier import ProofVerifier


def test_age_proof_flow():
    builder = CircuitBuilder()
    circuit = builder.create_circuit("age_test")

    circuit.add_public_input("age_limit", 18)
    circuit.add_private_input("user_age", 25)
    circuit.add_constraint("user_age >= age_limit")

    prover = ProofGenerator()
    proof = prover.generate_proof(circuit)

    verifier = ProofVerifier()
    result = verifier.verify(proof)

    assert result.is_valid is True
