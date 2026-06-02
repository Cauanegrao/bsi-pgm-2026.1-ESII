from repositórios.repositorio_emprestimo import RepositorioEmprestimo
from serviços.notificador import Notificador
from serviços.servico_emprestimo import ServicoEmprestimo

def test_fluxo_registrar_devolver_com_componentes_reais():
    repositorio = RepositorioEmprestimo()
    notificador = Notificador()
    servico = ServicoEmprestimo(repositorio, notificador)
    
    sucesso = servico.registrar(equip_id=1, nome="Ana", email="ana@ufra.edu.br", dias=7)
    
    assert sucesso is True
    emprestimo = repositorio.buscar_por_id(1)
    assert emprestimo is not None
    assert emprestimo["equip_id"] == 1
