from abc import ABC, abstractmethod

class IRepositorioEmprestimo(ABC):
    @abstractmethod
    def buscar_equipamento(self, id: int):
        pass

    @abstractmethod
    def salvar_emprestimo(self, emprestimo) -> None:
        pass

    @abstractmethod
    def buscar_emprestimo(self, id: int):
        pass

    @abstractmethod
    def marcar_indisponivel(self, equip_id: int) -> None:
        pass

    @abstractmethod
    def marcar_disponivel(self, equip_id: int) -> None:
        pass

    @abstractmethod
    def marcar_devolvido(self, emprestimo_id: int) -> None:
        pass

    @abstractmethod
    def listar_em_atraso(self) -> list:
        pass

    @abstractmethod
    def proximo_id_emprestimo(self) -> int:
        pass
