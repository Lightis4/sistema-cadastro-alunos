from cadastro import cadastrar_aluno
from consultar import consultar_alunos
from editor import editar_aluno
from excluir import excluir_aluno

# Menu para realizar as operações
def main():
    while True:
        print("\n=== SISTEMA DE CADASTRO DE ALUNOS ===")
        print("1 - Cadastrar aluno")
        print("2 - Consultar alunos")
        print("3 - Editar aluno")
        print("4 - Excluir aluno")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_alunos()
        elif opcao == "3":
            editar_aluno()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
