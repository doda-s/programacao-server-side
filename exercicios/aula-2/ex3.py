if __name__ == "__main__":
    g = str(input("'f' ou 'm'?\n"))

    if g.lower() == 'f':
        print("Feminino")
    elif g.lower() == 'm':
        print("Masculino")
    else:
        print("Inválido")