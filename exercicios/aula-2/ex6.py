if __name__ == "__main__":
    n1 = int(input("Digite um numero inteiro\n"))
    n2 = int(input("Digite um numero inteiro\n"))
    n3 = int(input("Digite um numero inteiro\n"))

    
    if n1 == n2 and n1 == n3:
        print("Todos são iguais")
    elif n1 > n2 and n1 > n3:
        print(f"Maior: {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"Maior: {n2}")
    else:
        print(f"Maior: {n3}")
