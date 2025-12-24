from backend.core.zk_engine.examples.age_proof import build_circuit as age_circuit
from backend.core.zk_engine.examples.password_proof import build_circuit as password_circuit
from backend.core.zk_engine.examples.balance_proof import build_circuit as balance_circuit


def test_age_proof():
    circuit = age_circuit()
    assert circuit.verify() is True


def test_password_proof():
    circuit = password_circuit()
    assert circuit.verify() is True


def test_balance_proof():
    circuit = balance_circuit()
    assert circuit.verify() is True
