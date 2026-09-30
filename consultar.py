from cadastro import alunos

def consultar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Matrícula: {aluno['matricula']}")
