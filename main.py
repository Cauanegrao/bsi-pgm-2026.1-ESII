# Main: Mediar a interação com o usuário final.
from services.servico_emprestimo import ServicoEmprestimo

sistema = ServicoEmprestimo()

from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from services.servico_emprestimo import ServicoEmprestimo

repo = RepositorioEmprestimo()
notif = Notificador()
sistema = ServicoEmprestimo(repo, notif)

def exibir_menu():
    while True:
        print("\n--- SISTEMA DE EMPRÉSTIMOS UFRA v2.0 ---")
        print("1. Registrar Empréstimo")
        print("2. Devolver Equipamento")
        print("3. Listar Atrasados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_e = int(input("ID do Equipamento: "))
            nome = input("Nome do Aluno: ")
            email = input("E-mail: ")
            if sistema.registrar(id_e, nome, email, 7):
                print(">>> Sucesso! Verifique a simulação de e-mail acima.")
            else:
                print(">>> Erro: Equipamento indisponível ou inexistente.")

        elif opcao == "2":
            id_emp = int(input("ID do Empréstimo: "))
            if sistema.devolver(id_emp):
                print(">>> Equipamento devolvido com sucesso!")
            else:
                print(">>> Erro: Empréstimo não encontrado ou já devolvido.")

        elif opcao == "3":
            atrasados = sistema.listar_atrasados()
            if not atrasados:
                print(">>> Ninguém está em atraso hoje.")
            else:
                for emp in atrasados:
                    print(f"- Aluno: {emp['nome_aluno']} | Entrega: {emp['data_devolucao']}")

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    exibir_menu()
