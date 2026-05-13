# ServicoEmprestimo: Executar as regras de negócio de locação.

from datetime import date, timedelta

class ServicoEmprestimo:
    def __init__(self, repo, notificador):
        self.repo = repo
        self.notificador = notificador

    def registrar(self, equip_id: int, nome: str, email: str, dias: int):
        """Implementação do UC01: Registrar Empréstimo"""
        equip = self.repo.buscar_por_id(equip_id)
        if equip and equip["disponivel"]:
            equip["disponivel"] = False
            data_dev = date.today() + timedelta(days=dias)
            
            # Criamos o registro do empréstimo
            novo_emprestimo = {
                "id": len(self.repo.listar_todos()) + 1,
                "equip_id": equip_id,
                "nome_aluno": nome,
                "email_aluno": email,
                "data_devolucao": data_dev,
                "devolvido": False
            }
            
            self.repo.salvar(novo_emprestimo)
            self.notificador.enviar_confirmacao(email, equip["nome"])
            return True
        return False

    def devolver(self, emprestimo_id: int):
        """Implementação do UC02: Devolver Equipamento"""
        emprestimos = self.repo.listar_todos()
        for emp in emprestimos:
            if emp["id"] == emprestimo_id and not emp["devolvido"]:
                emp["devolvido"] = True
                # Avisa o repositório para liberar o equipamento
                equip = self.repo.buscar_por_id(emp["equip_id"])
                if equip:
                    equip["disponivel"] = True
                return True
        return False

    def listar_atrasados(self):
        """Implementação do UC03: Listar Atrasados"""
        hoje = date.today()
        atrasados = [e for e in self.repo.listar_todos() if e["data_devolucao"] < hoje and not e["devolvido"]]
        return atrasados
