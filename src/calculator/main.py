import calculating_functions
import input_utils

operations = {
    "1": calculating_functions.add,
    "2": calculating_functions.subtract,
    "3": calculating_functions.multiply,
    "4": calculating_functions.divide,
    "5": calculating_functions.exit_program,
}


def main():
    print("Start Calculator: ")
    while True:
        choice = input_utils.show_menu()
        if choice not in operations:
            print("Invalid choice")
            continue
        
        if choice == "5":
            operations[choice]()
            break    
        
        a, b = input_utils.get_two_numbers()
        result = operations[choice](a, b)
        print(result)
            
if __name__ == "__main__":
    main()