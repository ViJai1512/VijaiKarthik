class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calc = Calculator()
print("Add:", calc.add(10, 5))
print("Sub:", calc.sub(10, 5))
print("Mul:", calc.mul(10, 5))
print("Div:", calc.div(10, 5))