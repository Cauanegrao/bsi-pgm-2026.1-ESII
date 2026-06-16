class SistemaEmprestimosFacade:
    def __init__(self, servico_emprestimo, servico_multa, servico_elegibilidade):
        self._servico_emprestimo = servico_emprestimo
        self._servico_multa = servico_multa
        self._servico_elegibilidade = servico_elegibilidade

    def realizar_emprestimo_completo(self, aluno_email, qtd_ativos, codigo_equipamento, tipo_equipamento, modelo):
        if not self._servico_elegibilidade.verificar_elegibilidade_aluno(qtd_ativos, aluno_email):
            return "Aluno não elegível para empréstimo."
            
        from factory import EquipamentoFactory
        equipamento = EquipamentoFactory.criar(tipo_equipamento, codigo_equipamento, modelo)
        
        return self._servico_emprestimo.registrar_emprestimo(aluno_email, equipamento)

    def consultar_multa_atraso(self, dias_atraso, valor_dia, carencia=2):
        return self._servico_multa.calcular_multa_com_carencia(dias_atraso, valor_dia, carencia)
