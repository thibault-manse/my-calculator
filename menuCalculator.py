def save_history_log(num1, num2, operation, result):
    with open('calculation_history.log', 'a') as log_file:
        if operation == 1:
            log_file.write(f"{num1} + {num2} = {result}\n")
        if operation == 2:
            log_file.write(f"{num1} - {num2} = {result}\n")
        if operation == 3:
            log_file.write(f"{num1} x {num2} = {result}\n")
        if operation == 4:
            log_file.write(f"{num1} / {num2} = {result}\n")
        if operation == 5:
            log_file.write(f"{num1} % {num2} = {result}\n")
        if operation == 6:
            log_file.write(f"{num1} ^ {num2} = {result}\n")
        if operation == 7:
            log_file.write(f"Square root of {num1} = {result}\n")
        if operation == 8:
            log_file.write(f"{num1} // {num2} = {result}\n")

# Function to read the history from the log file
def read_history_log():
    try:
        with open('calculation_history.log', 'r') as log_file:
            content = log_file.read()
            print("\n=== Log File Content ===")
            print(content)
    except FileNotFoundError:
        print("The Log file does not exist.")
    except Exception as e:
        print(f"Error reading the Log file: {e}")

# Function to clear the history from the log file
def clear_history_log():
    try:
        with open('calculation_history.log', 'w') as log_file:
            pass  # Write nothing to clear the content
        print("\nThe history has been successfully cleared.")
    except Exception as e:
        print(f"Error deleting the history: {e}")

def calculator_menu():
    switch = 0  # switch

    while True:
        print("\n=== Calculator Menu: ===")
        print("\n1. Clear history")
        print("2. Read history")
        print("3. Calculate")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '4':
            print("Thank you for using the calculator! Bye.")
            break
        elif choice == '1':  # Clear history
            clear_history_log()
            print("History cleared.")
        elif choice == '2':  # Read history
            read_history_log()
            print("Read history")
        elif choice == '3':  # Calculate
            try:
                num1 = int(input("Enter your 1st number: "))  # first number to calculate
            except ValueError:
                print("Please enter a integer number")
            num2, operation, switch = choose_operator(switch)
            calculate(num1, num2, operation, result, flag3, switch)

        else:
            print("Invalid choice! Please enter a valid option.")
            continue

        # If the choice is 1, 2, or 3, no further input is required.
        if choice in ['1', '2', '3']:
            continue

def choose_operator(switch):
    # choice operator
    while switch == 0:
        try:
            operation = int(input("Choose an operator: \n 1 : + \n 2 : - \n 3 : x \n 4 : / \n 5 : % \n 6 : power \n 7 : square root \n 8 : floor division \n"))
        except ValueError:
            print("Please enter an integer")
        else:
            if operation < 0 or operation > 8:
                print("Invalid choice")
            else:
                switch = 1

    switch2 = 0
    # if operator is square root
    if operation != 7:
        while switch2 == 0:
            try:
                num2 = int(input("Enter your 2nd number: "))
            except ValueError:
                print("Please enter an integer")
            if num2 == 0 and (operation == 4 or operation == 5 or operation == 8):
                print("This calculation is not possible with 0!")
            else:
                switch2 = 1
    else:
        num2 = 0

    switch = 0
    operator_data = (num2, operation, switch)  # tuple with num2, the operator and switch
    return operator_data

result = 0
flag3 = 0

def calculate(num1, num2, operation, result, flag3, switch):  # function to calculate with choice to continue or not
    if flag3 == 0:  # if it's the first calculation
        if operation == 1:
            result = num1 + num2
            print(num1, "+", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 2:
            result = num1 - num2
            print(num1, "-", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 3:
            result = num1 * num2
            print(num1, "x", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 4:
            result = num1 / num2
            print(num1, "/", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 5:
            result = num1 % num2
            print(num1, "%", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 6:
            result = num1 ** num2
            print(num1, "^", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 7:
            result = num1 ** 0.5
            print("Square root of ", num1, "=", result)
            save_history_log(num1, num2, operation, result)
        if operation == 8:
            result = num1 // num2
            print(num1, "//", num2, "=", result)
            save_history_log(num1, num2, operation, result)
        flag3 = 1

    elif flag3 == 1:  # if it's not the first calculation
        result_prev = result
        if operation == 1:
            result = result + num2
            print(result_prev, "+", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 2:
            result = result - num2
            print(result_prev, "-", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 3:
            result = result * num2
            print(result_prev, "x", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 4:
            result = result / num2
            print(result_prev, "/", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 5:
            result = result % num2
            print(result_prev, "%", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 6:
            result = result ** num2
            print(result_prev, "^", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 7:
            result = result ** 0.5
            print("Square root of ", result_prev, "=", result)
            save_history_log(result_prev, num2, operation, result)
        if operation == 8:
            result = result // num2
            print(result_prev, "//", num2, "=", result)
            save_history_log(result_prev, num2, operation, result)

    # choice to continue the calculation or not
    try:
        choice = str(input("Do you want to continue the calculation? (Y or N) ")).upper()
    except ValueError:
        print("Invalid value")
    except choice != "Y" or choice != "N":
        print("Please enter a valid value (Y or N)")

    if choice == "Y":
        num2, operation, switch = choose_operator(switch)
        calculate(num1, num2, operation, result, flag3, switch)
    elif choice == "N":
        return 0

if __name__ == "__main__":
    read_history_log()
    calculator_menu()
