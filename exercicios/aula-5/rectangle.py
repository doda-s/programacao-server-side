class Rectangle:
    def __init__(self, base, height):
        self._base = base
        self._height = height
        
    def sides(self):
        return f"{self.base} x {self.height}"
    
    def change_sides(self, base, height):
        self._base = base
        self._height = height
    
    def calc_area(self):
        return self._base * self._height
    
    def calc_perimeter(self):
        return self._base*2 + self._height*2