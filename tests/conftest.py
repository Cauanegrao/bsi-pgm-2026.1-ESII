import pytest
import datetime
from repositórios.interfaces import IRepositorioEmprestimo
from serviços.interfaces import INotificador
from serviços.servico_emprestimo import ServicoEmprestimo

# Fake — Implementação simplificada funcional que guarda dados em memória
class RepositorioFake(IRepositorioEmprestimo):
    def __init__(self):
        # Simulando uma lista de dicionários igual à do teu repositório real
        self.equipamentos = [
            {"id": 1, "nome": "Notebook Dell", "tipo": "Notebook", "disponivel": True},
            {"id": 2, "nome": "Projetor Epson", "tipo": "Projetor", "disponivel": True},
            {"id": 3, "nome": "Cabo HDMI", "tipo": "Cabo", "disponivel": True}
        ]
        self.emprestimos = []

    def buscar_equipamento(self, id):
        return next((e for e in self.equipamentos if e["id"] == id), None)

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def buscar_emprestimo(self, id):
        return next((e for e in self.emprestimos if e["id"] == id), None)

    def marcar_indisponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip["disponivel"] = False

    def marcar_disponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip["disponivel"] = True

    def marcar_devolvido(self, emprestimo_id):
        emp = self.buscar_emprestimo(emprestimo_id)
        if emp:
            emp["devolvido"] = True

    def listar_em_atraso(self):
        hoje = datetime.date.today()
        return [e for e in self.emprestimos if not e.get("devolvido", False) and e.get("data_devolucao", hoje) < hoje]

    def proximo_id_emprestimo(self):
        return len(self.emprestimos) + 1

# Spy — Grava as chamadas de envio de e-mail para fazermos os asserts depois
class NotificadorSpy(INotificador):
    def __init__(self):
        self.eventos = []

    def notificar_emprestimo(self, email, data_devolucao):
        self.eventos.append(("emprestimo", email, data_devolucao))

    def notificar_devolucao(self, email, multa):
        self.eventos.append(("devolucao", email, multa))

    def notificar_atraso(self, email):
        self.eventos.append(("atraso", email))

@pytest.fixture
def repositorio_fake():
    return RepositorioFake()

@pytest.fixture
def notificador_spy():
    return NotificadorSpy()

@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    return ServicoEmprestimo(repositorio_fake, notificador_spy)
