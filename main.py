class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is {result}")
    def __del__(self):
        print(f"Expression object with values {self.num1}, {self.num2}, and {self.num3} are removed.")

e1 = Expression(10, 20, 30)
e1.add_numbers()

e2 = Expression(5, 15, 25)
e2.add_numbers() 