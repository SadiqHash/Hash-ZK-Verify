"""
circuit_builder.py

Defines the core abstraction for a Zero-Knowledge circuit.
This module does not implement real ZK math yet.
It only defines structure, constraints, and intent.
"""

from typing import Dict, Any, List


class ZKCircuit:
    """
    Represents a Zero-Knowledge circuit.

    A circuit contains:
    - public inputs (known to verifier)
    - private inputs (witness / secret)
    - constraints (rules that must hold)
    """

    def __init__(self, name: str):
        self.name = name
        self.public_inputs: Dict[str, Any] = {}
        self.private_inputs: Dict[str, Any] = {}
        self.constraints: List[str] = []

    def verify(self) -> bool:
        """
        Temporary verification stub.

        For now:
        - Checks that constraints exist
        - Always returns True

        Later:
        - This will run real ZK proof verification
        """
        if not self.constraints:
            return False
        return True

    def add_public_input(self, key: str, value: Any) -> None:
        self.public_inputs[key] = value

    def add_private_input(self, key: str, value: Any) -> None:
        self.private_inputs[key] = value

    def add_constraint(self, description: str) -> None:
        """
        Constraint is stored as a human readable description for now.
        Later this will become an arithmetic constraint system.
        """
        self.constraints.append(description)

    def summary(self) -> Dict[str, Any]:
        """
        Returns a high level description of the circuit.
        Useful for debugging and education.
        """
        return {
            "name": self.name,
            "public_inputs": list(self.public_inputs.keys()),
            "private_inputs": list(self.private_inputs.keys()),
            "constraints_count": len(self.constraints),
        }


class CircuitBuilder:
    """
    High level builder interface for constructing ZK circuits.
    """

    def create_circuit(self, name: str) -> ZKCircuit:
        return ZKCircuit(name=name)
