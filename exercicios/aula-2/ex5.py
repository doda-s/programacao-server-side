if __name__ == "__main__":
    nota1 = float(input("Digite a primeira nota de um aluno\n"))
    nota2 = float(input("Digite a segunda nota de um aluno\n"))
    media = (nota1+nota2)/2

    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")