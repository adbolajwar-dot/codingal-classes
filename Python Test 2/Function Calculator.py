print("Welcome to the Calculator!")

def Add(x,y):
    return x + y
def Subtract(x,y):
    return x - y
def Multiply(x,y):
    return x * y
def Divide(x,y):
    if y == 0:
        print("Error! Division by zero is not allowed.")
    return x / y

while True:
    print("select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thank you for using the Calculator!")
        break

    if choice in {'1', '2', '3', '4'}:
        try:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {Add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {Subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {Multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {Divide(num1, num2)}")
        else:
                print("Invalid input! Please enter a valid number.")




