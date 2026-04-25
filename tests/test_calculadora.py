from src.calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(5, 3) == 2

def test_multiplicacao():
    assert multiplicacao(2, 4) == 8

def test_divisao():
    assert divisao(10, 2) == 5

def test_divisao_por_zero():
    try:
        divisao(10, 0)
        assert False
    except ZeroDivisionError:
        assert True
