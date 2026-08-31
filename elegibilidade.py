def verificar_elegibilidade_aluno(qtd_emprestimos_ativos, email):
    dentro_do_limite = qtd_emprestimos_ativos < 3
    eh_institucional = email.endswith("@ufra.edu.br")
    
    return dentro_do_limite and eh_institucional
