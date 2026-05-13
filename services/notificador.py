# Notificador: Processar o envio de comunicações externas.

class Notificador:
    def enviar_confirmacao(self, email: str, item: str):
        """Simula o envio de um e-mail de sucesso após o registro."""
        print("-" * 30)
        print(f"[SIMULAÇÃO DE EMAIL]")
        print(f"Para: {email}")
        print(f"Assunto: Confirmação de Empréstimo")
        print(f"Mensagem: Olá! O item '{item}' foi reservado com sucesso.")
        print("-" * 30)

    def enviar_alerta_atraso(self, email: str, multa: float):
        """Simula o envio de um alerta quando há atraso na devolução."""
        print("-" * 30)
        print(f"[SIMULAÇÃO DE EMAIL]")
        print(f"Para: {email}")
        print(f"Assunto: Alerta de Atraso!")
        print(f"Mensagem: Atenção! Seu empréstimo está atrasado. Multa atual: R$ {multa:.2f}")
        print("-" * 30)
