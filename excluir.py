from cadastro import alunos

def excluir_aluno():
    if not alunos:
        print("Nenhum aluno para excluir.")
        return

    matricula = input("Digite a matrícula do aluno que deseja excluir: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("Aluno excluído com sucesso!")
            return
    print("Aluno não encontrado.")
