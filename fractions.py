import math
class Fractions:
    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError('Wrong input. A should be integer')
        if not isinstance(b, int):
            raise TypeError('Wrong input. B should be integer')
        if not b:
            raise ZeroDivisionError("B can't be equal 0")
        self.__a = a
        self.__b = b

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
            return self.__a * other.__b == other.__a * self.__b
        if isinstance(other, float):
            return (self.__a / self.__b) == other
        return self.__a * other.__b == other.__a * self.__b

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, int | float):
            return (self.__a / self.__b) > other
        return (self.__a / self.__b) > (other.__a / other.__b)

    def __lt__(self, other):
        if isinstance(other, int | float):
            return (self.__a / self.__b) < other
        return (self.__a / self.__b) < (other.__a / other.__b)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = (self.__a * other.__b + other.__a * self.__b)
        denominator = (self.__b * other.__b)
        return Fractions(numerator, denominator)

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = (self.__a * other.__b + other.__a * self.__b)
        denominator = (self.__b * other.__b)
        return Fractions(numerator, denominator)

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = (self.__a * other.__b + other.__a * self.__b)
        denominator = (self.__b * other.__b)
        return Fractions(numerator, denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = (self.__a * other.__b - other.__a * self.__b)
        denominator = (self.__b * other.__b)
        return Fractions(numerator, denominator)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = (self.__a * other.__b - other.__a * self.__b)
        denominator = (self.__b * other.__b)
        return Fractions(numerator, denominator)

    def __isub__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = (self.__a * other.__b - other.__a * self.__b)
        denominator = (self.__b * other.__b)
        return Fractions(numerator, denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = self.__a * other.__a
        denominator = self.__b * other.__b
        return Fractions(numerator, denominator)

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = self.__a * other.__a
        denominator = self.__b * other.__b
        return Fractions(numerator, denominator)

    def __imul__(self, other):
        if isinstance(other, int):
            other = Fractions(other, 1)
        numerator = self.__a * other.__a
        denominator = self.__b * other.__b
        return Fractions(numerator, denominator)


    def __str__(self):
        gcd = math.gcd(self.__a, self.__b)
        self.__a //= gcd
        self.__b //= gcd
        if self.__a == self.__b:
            return f'1'
        if self.__b == 1:
            return f'{self.__a}'
        if self.__a > self.__b:
            return f'{self.__a // self.__b} {self.__a % self.__b}/{self.__b}'
        return f'{self.__a}/{self.__b}'


a = Fractions(-1, 3)
b = Fractions(-1, 2)
print(a)
print(b)

print(a+b)
print(a-b)
print(a*b)
print(a != 0.6)



