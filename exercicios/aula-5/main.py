from ball import Ball
from square import Square
from rectangle import Rectangle
from persons import Person

if __name__ == "__main__":
    
    # Classe bola
    ball = Ball("red", 2, "iron")
    ball.display_color()
    
    # Classe quadrado
    square = Square(2)
    print(f"Area do quadrado: {square.calc_area():.2f}m²")
    print(f"Lado atual do quadrado: {square.side:.2f}m")
    square.side = 6
    print(f"Novo lado do quadrado: {square.side:.2f}m")
    print(f"Nova área do quadrado: {square.calc_area()}m²")
    
    # Classe retângulo
    rectangle = Rectangle(float(input("Base do retângulo: ")), float(input("Altura do retângulo: ")))
    print(f"Quantidade de pisos (1m): {rectangle.calc_area()}")
    print(f"Comprimento total de rodapés: {rectangle.calc_perimeter()}m")
    
    # Classe Pessoa
    person = Person("Pablito", 20, 72, 180)
    print(
        f"Name: {person.name}\n",
        f"Age: {person.age}\n",
        f"Weight: {person.weight}\n",
        f"Height: {person.height}\n"
    )
    
    person.grow_old()
    person.get_fat()
    
    print(
        f"Name: {person.name}\n",
        f"Age: {person.age}\n",
        f"Weight: {person.weight}\n",
        f"Height: {person.height}\n"
    )