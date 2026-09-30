alunos = []

alunos = []


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")

    # Valida que a idade o Aluno so podera colocar numéros
    while True:
        idade = input("Digite a idade do aluno: ")
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print("A idade precisa ser um número. Tente novamente.")

    matricula = input("Digite o número de matrícula: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
