if __name__ == "__main__":
    num = int(input("DIGITE UM NÚMERO INTEIRO\n"))

    if not num < 0:
        print(f"O número '{num}' é positivo")
    else:
        print(f"O número '{num}' é negativo")