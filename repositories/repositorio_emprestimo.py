# RepositorioEmprestimo: Gerenciar o armazenamento dos dados do sistema.

class RepositorioEmprestimo:
    def __init__(self):
        self.equipamentos = [
            {"id": 1, "nome": "Notebook Dell", "tipo": "Notebook", "disponivel": True},
            {"id": 2, "nome": "Projetor Epson", "tipo": "Projetor", "disponivel": True}
        ]
        self.emprestimos = []

    def buscar_por_id(self, id: int):
        """Localiza um equipamento no inventário pelo ID."""
        return next((e for e in self.equipamentos if e["id"] == id), None)

    def salvar(self, objeto):
        """Adiciona um novo empréstimo à lista de registos."""
        self.emprestimos.append(objeto)

    def listar_todos(self):
        """Retorna todos os empréstimos registados."""
        return self.emprestimos
