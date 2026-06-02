# RepositorioEmprestimo: Gerenciar o armazenamento dos dados do sistema.
from repositórios.interfaces import IRepositorioEmprestimo

class RepositorioEmprestimo(IRepositorioEmprestimo):
    def __init__(self):
        # Banco de dados temporário (em memória)
        self.equipamentos = [
            {"id": 1, "nome": "Notebook Dell", "tipo": "Notebook", "disponivel": True},
            {"id": 2, "nome": "Projetor Epson", "tipo": "Projetor", "disponivel": True}
        ]
        self.emprestimos = []

    def buscar_por_id(self, id: int):
        return next((e for e in self.equipamentos if e["id"] == id), None)

    def salvar(self, objeto):
        self.emprestimos.append(objeto)

    def listar_todos(self):
        return self.emprestimos
