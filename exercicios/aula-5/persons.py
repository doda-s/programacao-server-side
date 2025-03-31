class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def grow_old(self):
        self.grow_up()
        self.age += 1
    
    def grow_up(self):
        if self.age < 21:
            self.height += 5
    
    def get_fat(self):
        self.weight += 1
    
    def lose_weight(self):
        self.weight -= 1