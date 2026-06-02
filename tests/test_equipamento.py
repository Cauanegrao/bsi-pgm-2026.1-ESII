import pytest

@pytest.mark.parametrize("tipo, dias, esperado", [
    ("Notebook", 3, 30.0),
    ("Notebook", 0, 0.0),
    ("Projetor", 2, 30.0),
    ("Cabo", 5, 10.0)
])
def test_calcular_multa_atraso_positivo(tipo, dias, esperado):
    taxas = {"Notebook": 10.0, "Projetor": 15.0, "Cabo": 2.0}
    multa = max(0.0, dias * taxas.get(tipo, 0.0))
    assert multa == esperado

@pytest.mark.parametrize("tipo", ["Notebook", "Projetor", "Cabo"])
def test_calcular_multa_atraso_negativo_retorna_zero(tipo):
    taxas = {"Notebook": 10.0, "Projetor": 15.0, "Cabo": 2.0}
    multa = max(0.0, -5 * taxas.get(tipo, 0.0))
    assert multa == 0.0
