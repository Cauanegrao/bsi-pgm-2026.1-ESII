# Main: Mediar a interação com o utilizador final.

from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.notificador import Notificador
from services.servico_emprestimo import ServicoEmprestimo

def exibir_menu():
    repo_concreto = RepositorioEmprestimo()
    notificador_concreto = Notificador()

    sistema = ServicoEmprestimo(repo_concreto, notificador_concreto)

    while True:
        print("\n--- SISTEMA DE EMPRÉSTIMOS UFRA v2.0 ---")
        print("1. Registrar Empréstimo")
        print("2. Devolver Equipamento")
        print("3. Listar Atrasados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id_e = int(input("ID do Equipamento: "))
                nome = input("Nome do Aluno: ")
                email = input("E-mail: ")
                # O sistema usa 7 dias como padrão para o empréstimo
                if sistema.registrar(id_e, nome, email, 7):
                    print(">>> Sucesso! Verifique a simulação de e-mail acima.")
                else:
                    print(">>> Erro: Equipamento indisponível ou inexistente.")
            except ValueError:
                print(">>> Erro: O ID deve ser um número inteiro.")

        elif opcao == "2":
            try:
                id_emp = int(input("ID do Empréstimo: "))
                if sistema.devolver(id_emp):
                    print(">>> Equipamento devolvido com sucesso!")
                else:
                    print(">>> Erro: Empréstimo não encontrado ou já devolvido.")
            except ValueError:
                print(">>> Erro: O ID deve ser um número inteiro.")

        elif opcao == "3":
            atrasados = sistema.listar_atrasados()
            if not atrasados:
                print(">>> Não existem empréstimos em atraso.")
            else:
                print("\n--- LISTA DE ATRASADOS ---")
                for emp in atrasados:
                    print(f"- Aluno: {emp['nome_aluno']} | Item: {emp['item_nome']} | Entrega: {emp['data_devolucao']}")

        elif opcao == "4":
            print("A encerrar o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    exibir_menu()
