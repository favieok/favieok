def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

while True:
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == "+":
        print(add(num1, num2))
    elif op == "-":
        print(sub(num1, num2))
    elif op == "*":
        print(mul(num1, num2))
    elif op == "/":
        print(div(num1, num2))
    else:
        print("Invalid Operator!")

    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
        break

