import math

class Vertor:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, item):
        x = self.x + item.x
        y = self.y + item.y
        return Vertor(x, y)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __mul__(self, item):
        return Vertor(self.x * item, self.y * item )

    def __repr__(self) -> str:
        return f"Vertor {self.x=} {self.y!r}" # !r:repr(), 如果是字符, 则有''包括 !a: ascii() !s:str() =: self.x=值 

v1 = Vertor(3, 4)
v2 = Vertor(6, 9)

v3 = v1 + v2
abs(v1)
v1 * 3
print(v1)
