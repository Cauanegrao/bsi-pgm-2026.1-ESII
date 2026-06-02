# ServicoEmprestimo: Executar as regras de negócio de locação.
from repositórios.interfaces import IRepositorioEmprestimo
from serviços.interfaces import INotificador
from datetime import date, timedelta

class ServicoEmprestimo:
    def __init__(self, repositorio: IRepositorioEmprestimo, notificador: INotificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equip_id: int, nome: str, email: str, dias: int) -> bool:
        equip = self.repositorio.buscar_equipamento(equip_id)
        if equip and equip.get("disponivel", True):
            self.repositorio.marcar_indisponivel(equip_id)
            data_dev = date.today() + timedelta(days=dias)
            
            novo_emprestimo = {
                "id": self.repositorio.proximo_id_emprestimo(),
                "equip_id": equip_id,
                "nome_aluno": nome,
                "email_aluno": email,
                "data_devolucao": data_dev,
                "devolvido": False
            }
            
            self.repositorio.salvar_emprestimo(novo_emprestimo)
            self.notificador.notificar_emprestimo(email, data_dev)
            return True
        return False

    def devolver(self, emprestimo_id: int) -> float:
        emp = self.repositorio.buscar_emprestimo(emprestimo_id)
        if emp and not emp.get("devolvido", False):
            self.repositorio.marcar_devolvido(emprestimo_id)
            self.repositorio.marcar_disponivel(emp["equip_id"])
            return 0.0  
        return 0.0

    def listar_atrasados(self) -> list:
        return self.repositorio.listar_em_atraso()
