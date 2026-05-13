# Notificador: Processar o envio de comunicações externas.

class Notificador:
    def enviar_confirmacao(self, email: str, item: str):
        print(f"\n[EMAIL] Enviado para: {email}")
        print(f"Mensagem: O item '{item}' foi reservado com sucesso.")

    def enviar_alerta_atraso(self, email: str, multa: float):
        print(f"\n[EMAIL] Alerta para: {email}")
        print(f"Atenção: Devolução em atraso. Multa: R$ {multa:.2f}")
