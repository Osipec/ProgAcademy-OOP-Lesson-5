class Square:
    def __init__(self, side_a: int | float, side_b: int | float):
        if not isinstance(side_a, int | float) or side_a <= 0:
            raise TypeError('Incorrect input data type(side A)')
        if not isinstance(side_b, int | float) or side_b <= 0:
            raise TypeError('Incorrect input data type(side B)')
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __add__(self, other):
        if isinstance(other, Square):
            return self.area() + other.area()
        if isinstance(other, int | float):
            return self.area() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int | float):
            return self.area() + other
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.area() * other
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int | float):
            return self.area() * other
        return NotImplemented

    def __str__(self):
        return f'{self.side_a} x {self.side_b}'

a = Square(2, 3)
b = Square(3,2)
c = Square(1, 2)
print(a)
print(b)
print(c)
print(a+b+c+2)
print(a*2)
print(a==b)
