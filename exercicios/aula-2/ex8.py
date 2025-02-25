if __name__ == "__main__":
    n1 = float(input("Digite o preço de um produto\n"))
    n2 = float(input("Digite o preço de um produto\n"))
    n3 = float(input("Digite o preço de um produto\n"))

    
    if n1 == n2 and n1 == n3:
        print("Todos os preços são iguais")
    elif n1 < n2 and n1 < n3:
        print(f"Menor preço: {n1:.2}")
    elif n2 < n1 and n2 < n3:
        print(f"Menor preço: {n2:.2}")
    else:
        print(f"Menor preço: {n3:.2}")
