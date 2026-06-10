import pytest
from elegibilidade import verificar_elegibilidade_aluno

def test_aluno_sem_emprestimos_ativos_esta_elegivel():
    resultado = verificar_elegibilidade_aluno(qtd_emprestimos_ativos=0, email="caua@ufra.edu.br")
    assert resultado is True
