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
            
            novo_emprestimo = {
                "id": len(self.repo.listar_todos()) + 1,
                "nome_aluno": nome,
                "email_aluno": email,
                "item_nome": equip["nome"],
                "data_devolucao": data_dev,
                "devolvido": False
            }
            
            self.repo.salvar(novo_emprestimo)
            self.notificador.enviar_confirmacao(email, equip["nome"])
            return True
        return False

    def devolver(self, emprestimo_id: int):
        for emp in self.repo.listar_todos():
            if emp["id"] == emprestimo_id and not emp["devolvido"]:
                emp["devolvido"] = True
                equip = self.repo.buscar_por_id(emp["equip_id"])
                if equip: equip["disponivel"] = True
                return True
        return False

    def listar_atrasados(self):
        hoje = date.today()
        return [e for e in self.repo.listar_todos() if e["data_devolucao"] < hoje and not e["devolvido"]]
