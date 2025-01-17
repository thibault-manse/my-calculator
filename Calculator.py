"""
function log history calculator
"""


def save_history_log(nb1, nb2, ope, result):
    with open('calculation_history.log', 'a') as log_file:
        if ope == 1:
            log_file.write(f"{nb1} + {nb2} = {result}\n")
        if ope == 2:
            log_file.write(f"{nb1} - {nb2} = {result}\n")
        if ope == 3:
            log_file.write(f"{nb1} x {nb2} = {result}\n")
        if ope == 4:
            log_file.write(f"{nb1} / {nb2} = {result}\n")
        if ope == 5:
            log_file.write(f"{nb1} % {nb2} = {result}\n")
        if ope == 6:
            log_file.write(f"{nb1} ^ {nb2} = {result}\n")
        if ope == 7:
            log_file.write(f"Racine de {nb1} = {result}\n")
        if ope == 8:
            log_file.write(f"{nb1} // {nb2} = {result}\n")

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


"""
function calculator
"""


def calculator_menu():
    flag = 0  # switch

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
            while True:
                # Choice between int or float number
                int_and_float = str(input(
                    "Would you like to calculate with integers or decimal numbers? (INt ou FLOAT) ")).upper()
                if int_and_float != "INT" and int_and_float != "FLOAT" and int_and_float != "I" and int_and_float != "F":
                    print("Enter INT ou FLOAT")
                else:
                    break
            if int_and_float == "INT" or int_and_float == "I":
                try:
                    # fisrt number to calculate
                    nb1 = int(input("Enter your first number : "))
                except ValueError:
                    print("Enter an integer, please.")
                nb2, ope, flag = operator(flag, int_and_float)
                calc(nb1, nb2, ope, result, flag3, flag, int_and_float)
            elif int_and_float == "FLOAT" or int_and_float == "F":
                try:
                    nb1 = float(input("Enter your first number : "))
                except ValueError:
                    print(
                        "Enter a floating-point number, please (using a dot, not a comma)")
                nb2, ope, flag = operator(flag, int_and_float)
                calc(nb1, nb2, ope, result, flag3, flag, int_and_float)

        else:
            print("Invalid choice! Please enter a valid option.")
            continue

        # If the choice is 1, 2, or 3, no further input is required.
        if choice in ['1', '2', '3']:
            continue


def operator(flag, int_and_float):
    # choice operator
    while flag == 0:
        try:
            ope = int(input(
                "Choose an operator : \n 1 : + \n 2 : - \n 3 : x \n 4 : / \n 5 : % \n 6 : power \n 7 : root \n 8 : Euclidien div.  \n"))
        except ValueError:
            print("Enter an integer, please.")
        else:
            if ope < 0 or ope > 8:
                print("Invalid choice")
            else:
                flag = 1

    flag2 = 0
    # if operator is square root + int and float value
    if ope != 7:
        if int_and_float == "INT" or int_and_float == "I":
            while flag2 == 0:
                try:
                    nb2 = int(input("Enter your second number: "))
                except ValueError:
                    print("Enter an integer, please.")
                if nb2 == 0 and (ope == 4 or ope == 5 or ope == 8):
                    print("This calculation is impossible with 0. !")
                else:
                    flag2 = 1
        elif int_and_float == "FLOAT" or int_and_float == "F":
            while flag2 == 0:
                try:
                    nb2 = float(input("Enter your second number : "))
                except ValueError:
                    print("Please enter a floating-point number.")
                if nb2 == 0 and (ope == 4 or ope == 5 or ope == 8):
                    print("This calculation is impossible with 0. !")
                else:
                    flag2 = 1
    else:
        nb2 = 0

    flag = 0
    list = (nb2, ope, flag)  # tuple with number2, the operator and switch
    return list


result = 0
flag3 = 0


# function calculator with choice to continue or not
def calc(nb1, nb2, ope, result, flag3, flag, int_and_float):
    if flag3 == 0:  # if it's the first calculation
        if ope == 1:
            result = nb1 + nb2
            print(nb1, "+", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 2:
            result = nb1 - nb2
            print(nb1, "-", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 3:
            result = nb1 * nb2
            print(nb1, "x", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 4:
            result = nb1 / nb2
            print(nb1, "/", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 5:
            result = nb1 % nb2
            print(nb1, "%", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 6:
            result = nb1 ** nb2
            print(nb1, "^", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 7:
            result = nb1 ** 0.5
            print("Square root of ", nb1, "=", result)
            save_history_log(nb1, nb2, ope, result)
        if ope == 8:
            result = nb1 // nb2
            print(nb1, "//", nb2, "=", result)
            save_history_log(nb1, nb2, ope, result)
        flag3 = 1

    elif flag3 == 1:  # if it's not the first calculation
        result_prev = result
        if ope == 1:
            result = result + nb2
            print(result_prev, "+", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 2:
            result = result - nb2
            print(result_prev, "-", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 3:
            result = result * nb2
            print(result_prev, "x", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 4:
            result = result / nb2
            print(result_prev, "/", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 5:
            result = result % nb2
            print(result_prev, "%", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 6:
            result = result ** nb2
            print(result_prev, "^", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 7:
            result = result ** 0.5
            print("Square root of ", result_prev, "=", result)
            save_history_log(result_prev, nb2, ope, result)
        if ope == 8:
            result = result // nb2
            print(result_prev, "//", nb2, "=", result)
            save_history_log(result_prev, nb2, ope, result)

    # choice to continue the calculation or not
    while True:
        try:
            choice = str(input("Continue the calculation? (Y ou N) ")).upper()
        except ValueError:
            print("Invalid value")
        if choice != "Y" and choice != "N":
            print("Enter a valid value (Y ou N)")
        else:
            break

    if choice == "Y":
        nb2, ope, flag = operator(flag, int_and_float)
        calc(nb1, nb2, ope, result, flag3, flag, int_and_float)
    elif choice == "N":
        return 0


if __name__ == "__main__":
    read_history_log()
    calculator_menu()
