if __name__ == "__main__":
    list_of_items = ["hello world", 416, True, 3.14]
    type_map = {'int': int, 'float': float, "str": str, 'bool': bool}
    
    selection = int(input(f"Selecione um elemento de 1 até {len(list_of_items)}\n>> "))
    
    if selection < 1 and selection > len(list_of_items):
        print("Opção inválida!")
    else:
        value_type = str(input(f"Qual é o tipo desse valor? -> {list_of_items[selection-1]}\n>> "))
        
        if isinstance(list_of_items.pop(selection-1), type_map.get(value_type.lower())):
            print("Você acertou!")
        else:
            print("Você errou! :c")