from src.calculadora import soma, eh_par


def test_soma():
    assert soma(2, 3) == 5


def test_eh_par():
    assert eh_par(4) is True
    assert eh_par(5) is False

def test_soma_zero():
    assert soma(0, 0) == 0