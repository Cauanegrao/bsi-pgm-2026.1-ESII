# ServicoEmprestimo: Executar as regras de negócio de locação.

from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from datetime import date, timedelta

class ServicoEmprestimo:
    def __init__(self):
        self.repo = RepositorioEmprestimo()
        self.notificador = Notificador()

    def registrar(self, equip_id: int, nome: str, email: str, dias: int):
        equip = self.repo.buscar_por_id(equip_id)
        if equip and equip["disponivel"]:
            equip["disponivel"] = False
            
            data_dev = date.today() + timedelta(days=dias)
            
            self.repo.salvar({"aluno": nome, "item": equip["nome"], "entrega": data_dev})
            self.notificador.enviar_confirmacao(email, equip["nome"])
            return True
        return False
