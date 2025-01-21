import json
import os

"""
function json history calculator
"""
# Function to save the history in a JSON file


def save_history_log(nb1, nb2, ope, result):
    # Determines the operator as a symbol
    operators = {1: '+', 2: '-', 3: 'x',
                 4: '/', 5: '%', 6: '^', 7: '√', 8: '//'}
    operator_symbol = operators.get(ope, '?')

    # Load the existing history or initialize an empty list
    history = []
    if os.path.exists('calculation_history.json'):
        with open('calculation_history.json', 'r') as file:
            history = json.load(file)

    # Add the new calculation to the history
    history.append({
        "value1": nb1,
        "operator": operator_symbol,
        "value2": nb2 if nb2 != 0 or ope == 7 else None,
        "result": result
    })

    # Save to the JSON file
    with open('calculation_history.json', 'w') as file:
        json.dump(history, file, indent=4)
    print("Calculation saved in history.")

# Function to read the history from the JSON file


def read_history_log():
    if not os.path.exists('calculation_history.json'):
        print("\nHistoric is empty.")
        return

    with open('calculation_history.json', 'r') as file:
        history = json.load(file)

    print("\n=== Calculation History ===")
    for entry in history:
        value2 = entry["value2"] if entry["value2"] is not None else ""
        print(f"{entry['value1']} {entry['operator']} {
              value2} = {entry['result']}")

# Function to clear the history from the JSON file


def clear_history_log():
    if os.path.exists('calculation_history.json'):
        os.remove('calculation_history.json')
        print("\nThe historic is clear.")
    else:
        print("\nNo historic to clear.")


"""
function calculator
"""

# Function for simple arithmetic operations
def calcul_long(ope, nb1, nb2):
    if ope == "+":
        result = nb1 + nb2
    elif ope == "-":
        result = nb1 - nb2
    elif ope == "*":
        result = nb1 * nb2
    elif ope == "/":
        if nb2 == 0:
            raise ZeroDivisionError("Division by zero detected.")
        result = nb1 / nb2
    else:
        raise ValueError(f"Operator unknown: {ope}")

    # Save the operation to history
    save_history_log(nb1, nb2, ["+", "-", "*", "/"].index(ope) + 1, result)
    return result

def compound_calculation():
    try:
        operations = [int(input("Put the first number : "))]
        pr_calc = [operations[0]]

        while True:
            calcul = input("You have the choice between : '+', '-', '*', '/' ou write fin end you can't anymore: ")
            if calcul == "end":
                while len(operations) > 1:
                    idx = next((i for i in range(1, len(operations), 2) if operations[i] in "*/"), None)
                    if idx is None:
                        idx = 1

                    # Perform the calculation
                    res = calcul_long(operations[idx], operations[idx - 1], operations[idx + 1])

                    # Save each intermediate step to the history
                    save_history_log(operations[idx - 1], operations[idx + 1], ["+", "-", "*", "/"].index(operations[idx]) + 1, res)

                    # Replace in the operations list
                    operations[idx - 1:idx + 2] = [res]

                print(f"Et le résultat est : {operations[0]}")
                # Save the final result to history
                save_history_log(pr_calc[0], 0, 0, operations[0])  # Last save without operator
                break

            if calcul in {"+", "-", "*", "/"}:
                following = int(input("Put the number : "))
                operations.append(calcul)
                pr_calc.append(calcul)
                operations.append(following)
                pr_calc.append(following)
                print(f"État actuel : {operations}")
            else:
                print("haven't i been clear, learn to read.")

    except ValueError:
        print("Erreur : put numbers and operators available.")
    except ZeroDivisionError:
        print("Erreur : Division by zero detected.")


def calculator_menu():
    flag = 0  # switch

    while True:
        print("\n=== Calculator Menu: ===")
        print("\n1. Clear history")
        print("2. Read history")
        print("3. Calculate")
        print("4. Compound calculation")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
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
                    "Would you like to calculate with integers or decimal numbers? (INT ou FLOAT) ")).upper()
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
        
        elif choice == '4':
            compound_calculation()
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
