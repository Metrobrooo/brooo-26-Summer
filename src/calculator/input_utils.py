def show_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return None


def get_two_numbers():
    a = None
    while a is None:
        try:
            a = int(input("Enter first number: "))
        except ValueError:
            print("Invalid input for first number")
            continue
    b = None
    while b is None:
        try:
            b = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input for second number")
            continue
    return a, b