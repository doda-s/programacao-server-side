class Square:
    def __init__(self, side: float):
        self._side = side

    @property
    def side(self):
        return self._side
    
    @side.setter
    def side(self, new_side: float):
        self._side = new_side
    
    def calc_area(self):
        return 4 * self._side