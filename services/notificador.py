# Notificador: Processar o envio de comunicações externas.
from serviços.interfaces import INotificador
from datetime import date

class Notificador(INotificador):
    def notificar_emprestimo(self, email: str, data_devolucao: date) -> None:
        # Usando a lógica do seu método enviar_confirmacao
        print(f"\n[EMAIL] Enviado para: {email}")
        print(f"Mensagem: Empréstimo registrado com sucesso. Data de devolução: {data_devolucao}")

    def notificar_devolucao(self, email: str, multa: float) -> None:
        # Usando a lógica do seu método enviar_alerta_atraso
        print(f"\n[EMAIL] Alerta para: {email}")
        print(f"Atenção: Devolução em atraso. Multa: R$ {multa:.2f}")

    def notificar_atraso(self, email: str) -> None:
        # Método obrigatório da interface para avisar sobre pendências
        print(f"\n[EMAIL] Alerta de pendência enviado para: {email}")
        print("Atenção: Você possui um equipamento em atraso!")
