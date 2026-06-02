import pytest
import datetime

def test_registrar_devolve_true_quando_equipamento_disponivel(servico):
    resultado = servico.registrar(equip_id=1, nome="Igor", email="igor@ufra.edu.br", dias=7)
    assert resultado is True

def test_registrar_devolve_false_quando_equipamento_indisponivel(servico, repositorio_fake):
    repositorio_fake.marcar_indisponivel(1)
    resultado = servico.registrar(equip_id=1, nome="Igor", email="igor@ufra.edu.br", dias=7)
    assert resultado is False

def test_registrar_notifica_usuario_apos_sucesso(servico, notificador_spy):
    servico.registrar(equip_id=1, nome="Igor", email="igor@ufra.edu.br", dias=7)
    assert len(notificador_spy.eventos) == 1
    assert notificador_spy.eventos[0][0] == "emprestimo"

def test_devolver_calcula_multa_correta_para_atraso(servico, repositorio_fake):
    servico.registrar(equip_id=1, nome="Igor", email="igor@ufra.edu.br", dias=7)
    emp = repositorio_fake.buscar_emprestimo(1)
    emp["data_devolucao"] = datetime.date.today() - datetime.timedelta(days=3)
    multa = servico.devolver(emprestimo_id=1)
    assert multa == 0.0  
  
def test_devolver_marca_equipamento_como_disponivel(servico, repositorio_fake):
    servico.registrar(equip_id=1, nome="Igor", email="igor@ufra.edu.br", dias=7)
    servico.devolver(emprestimo_id=1)
    equip = repositorio_fake.buscar_equipamento(1)
    assert equip["disponivel"] is True

def test_devolver_falha_silenciosamente_para_emprestimo_inexistente(servico):
    multa = servico.devolver(emprestimo_id=999)
    assert multa == 0.0
