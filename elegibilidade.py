def verificar_elegibilidade_aluno(qtd_emprestimos_ativos, email):
    if qtd_emprestimos_ativos >= 3:
        return False
    return True
