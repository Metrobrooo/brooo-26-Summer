import calculating_functions
import input_utils

operations = {
    "1": calculating_functions.add,
    "2": calculating_functions.subtract,
    "3": calculating_functions.multiply,
    "4": calculating_functions.divide,
    "5": "Exiting..."
}


def main():
    while True:
        print("Start Calculator: ")
        choice = input_utils.show_menu()
        if choice not in operations.keys():
            print("Invalid choice")
            continue
        if choice == "5":
            print(operations[choice])
            break
        a, b = input_utils.get_two_numbers()
        result = operations[choice](a, b)
        print(result)
            
if __name__ == "__main__":
    main()