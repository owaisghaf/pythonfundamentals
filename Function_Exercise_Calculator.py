def calculator():

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    a = float(input("enter first number > "))
    op_entry = input("Enter an Operator > + , - , * , /  ")
    b = float(input("enter second number > "))

    if op_entry == '+':
        print(f"{a} + {b} = {add(a, b)}")

    elif op_entry == '-':
        print(f"{a} - {b} = {subtract(a, b)}")

    elif op_entry == '*':
        print(f"{a} x {b} = {multiply(a, b)}")

    elif op_entry == '/':
        print(f"{a} / {b} = {divide(a, b)}")

    else:
        print("please enter the correct symbol")

    return calculator()


calculator()
