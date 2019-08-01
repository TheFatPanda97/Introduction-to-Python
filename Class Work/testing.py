import math


class Linear:
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def find_y(self, x):
        return self.m * x + self.b

    def closest_to_origin(self):
        smallest_distance = 1000000
        x, y = 0, 0
        for i in range(-1000, 1001):
            temp_d = math.sqrt(i ** 2 + self.find_y(i) ** 2)
            if temp_d < smallest_distance:
                smallest_distance = temp_d
                x, y = i, self.find_y(i)
        return x, y


# f = Linear(1, 0)
# print(f.closest_to_origin())

# print("hello".join(" "))
set_a = [1, 2, 3]
set_b = [4, 21]
print(list(set(set_a) & set(set_b)))
