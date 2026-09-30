from cadastro import alunos

def editar_aluno():
    if not alunos:
        print("Nenhum aluno para editar.")
        return

    matricula = input("Digite a matrícula do aluno que deseja editar: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("Aluno encontrado. Digite os novos dados:")
            aluno["nome"] = input("Novo nome: ")
            aluno["idade"] = input("Nova idade: ")
            print("Dados atualizados com sucesso!")
            return
    print("Aluno não encontrado.")
