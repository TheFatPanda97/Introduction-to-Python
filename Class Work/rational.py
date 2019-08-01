class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        common_d = self.denominator * other.denominator
        top = self.numerator * other.denominator + self.denominator * other.numerator
        return Rational(top, common_d)

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Rational(n, d)

    def reduce(self):
        largest = 1
        for i in range(1, min(self.denominator, self.numerator)):
            if self.numerator % i == 0 and self.denominator % i == 0:
                largest = i
        return Rational(self.numerator // largest, self.denominator // largest)

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)


num1 = Rational(1, 2)
num2 = Rational(1, 3)
ans = num1 + num2
print(ans.numerator)
print(ans)
