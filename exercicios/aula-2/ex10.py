if __name__ == "__main__":
    t = str(input("Qual turno você estuda?\n"+
                  "[M] - Matutino\n"+
                  "[V] - Vespertino\n"+
                  "[N] - Noturno\n"+
                  ">> "
                ))

    if t.lower() == 'm':
        print("Bom dia!")
    elif t.lower() == 'v':
        print("Boa tarde!")
    elif t.lower() == 'n':
        print("Boa noite!")
    else:
        print("Valor inválido!")