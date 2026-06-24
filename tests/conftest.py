from services.observer import Observer

class NotificadorSpy(Observer):
    def __init__(self):
        self.eventos = []
    def update(self, evento):
        self.eventos.append(evento)

@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    s = ServicoEmprestimo(repositorio_fake)
    s.registrar_observer(notificador_spy)
    return s
