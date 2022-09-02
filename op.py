# Program make a simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add 2.Subtract 3.Multiply 4.Divide")

while True:
    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")

