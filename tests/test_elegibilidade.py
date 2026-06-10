import pytest
from elegibilidade import verificar_elegibilidade_aluno

def test_aluno_sem_emprestimos_ativos_esta_elegivel():
    resultado = verificar_elegibilidade_aluno(qtd_emprestimos_ativos=0, email="caua@ufra.edu.br")
    assert resultado is True

def test_aluno_com_tres_ou_mais_emprestimos_fica_bloqueado():
    resultado = verificar_elegibilidade_aluno(qtd_emprestimos_ativos=3, email="caua@ufra.edu.br")
    assert resultado is False

def test_aluno_com_email_nao_institucional_fica_bloqueado():
    resultado = verificar_elegibilidade_aluno(qtd_emprestimos_ativos=0, email="caua@gmail.com")
    assert resultado is False
