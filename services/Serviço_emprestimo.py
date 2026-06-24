# ServicoEmprestimo: Executar as regras de negócio de locação.
from datetime import date, timedelta
from services.observer import Subject 

class ServicoEmprestimo(Subject): 
    def __init__(self, repositorio_emprestimo): 
        super().__init__() 
        self.repo = repositorio_emprestimo

    def registrar(self, equip_id: int, nome: str, email: str, dias: int):
        equip = self.repo.buscar_por_id(equip_id)
        if equip and equip["disponivel"]:
            equip["disponivel"] = False
            data_dev = date.today() + timedelta(days=dias)
            
            novo_emprestimo = {
                "id": len(self.repo.listar_todos()) + 1,
                "equip_id": equip_id,
                "nome_aluno": nome,
                "email_aluno": email,
                "item_nome": equip["nome"],
                "data_devolucao": data_dev,
                "devolvido": False
            }
            
            self.repo.salvar(novo_emprestimo)
            
            self.notificar({
                "tipo": "emprestimo", 
                "email": email, 
                "data": data_dev
            })
            
            return True
        return False

    def devolver(self, emprestimo_id: int):
        for emp in self.repo.listar_todos():
            if emp["id"] == emprestimo_id and not emp["devolvido"]:
                emp["devolvido"] = True
                equip = self.repo.buscar_por_id(emp["equip_id"])
                if equip: 
                    equip["disponivel"] = True

                multa = 0.0  
                self.notificar({
                    "tipo": "devolucao", 
                    "email": emp["email_aluno"], 
                    "multa": multa
                })
                
                return True
        return False

    def listar_atrasados(self):
        hoje = date.today()
        atrasados = [e for e in self.repo.listar_todos() if e["data_devolucao"] < hoje and not e["devolvido"]]
        
        for emp in atrasados:
            self.notificar({
                "tipo": "atraso", 
                "email": emp["email_aluno"]
            })
            
        return atrasados
