import pytest
from multa import calcular_multa_com_carencia

def test_multa_zero_quando_sem_atraso():
    multa = calcular_multa_com_carencia(dias_atraso=0, valor_dia=10.0)
    assert multa == 0.0

def test_multa_cobra_dias_excedentes_apos_carencia():
    multa = calcular_multa_com_carencia(dias_atraso=5, valor_dia=10.0)
    assert multa == 30.0
