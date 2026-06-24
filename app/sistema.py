from services.servico_emprestimo import ServicoEmprestimo
from services.notificador_email import NotificadorEmail

class SistemaDeEmprestimos:
    def __init__(self):
        self._repositorio = RepositorioEmprestimo()
        self._servico = ServicoEmprestimo(self._repositorio)
        self._servico.registrar_observer(NotificadorEmail())
