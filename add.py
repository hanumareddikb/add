class Calculate:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

obj = Calculate(num1, num2)
print("sum : ",obj.add())