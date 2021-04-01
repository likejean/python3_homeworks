# for letter in 'Python':
#     print(f'Current number is: {letter}')
#     print("Geeks: {a:5d},  Portal: {p:0.2f}".
#           format(a=453, p=59.058))

class MyClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply_numbers(self):
        return self.x * self.y

    @staticmethod
    def add_numbers(x, y):
        return x + y


# numbers = MyClass(4, 6)
# print(numbers.multiply_numbers())
print(MyClass.add_numbers(2, 5))
print(MyClass.add_numbers(2, 256))
