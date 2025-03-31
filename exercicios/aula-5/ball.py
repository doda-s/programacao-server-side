class Ball:
    
    def __init__(self, color: str, circunference: float, material: str):
        self._color = color
        self._circunference = circunference
        self._material = material
        
    def change_color(self, new_color: str):
        self._color = new_color
    
    def display_color(self):
        print(f"Cor da bola: {self._color}")