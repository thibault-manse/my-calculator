import json
import os

"""
Functions to manage JSON history
"""

# Function to save the history in a JSON file
def save_history_log(nb1, nb2, ope, result):
    # Determines the operator as a symbol
    operators = {1: '+', 2: '-', 3: 'x', 4: '/', 5: '%', 6: '^', 7: '√', 8: '//'}
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
        print(f"{entry['value1']} {entry['operator']} {value2} = {entry['result']}")

# Function to clear the history from the JSON file
def clear_history_log():
    if os.path.exists('calculation_history.json'):
        os.remove('calculation_history.json')
        print("\nThe historic is clear.")
    else:
        print("\nNo historic to clear.")


"""
Calculator functions
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
            raise ZeroDivisionError("Division par zéro détectée.")
        result = nb1 / nb2
    else:
        raise ValueError(f"Opérateur inconnu : {ope}")

    # Save the operation to history
    save_history_log(nb1, nb2, ["+", "-", "*", "/"].index(ope) + 1, result)
    return result

# Function for compound calculations
def compound_calculation():
    try:
        operations = [int(input("Entrez le premier nombre : "))]
        pr_calc = [operations[0]]

        while True:
            calcul = input("T'as le choix entre ces calculs : '+', '-', '*', '/' ou tape 'fin' si t'en peux plus : ")
            if calcul == "fin":
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
                following = int(input("Entre ton nombre : "))
                operations.append(calcul)
                pr_calc.append(calcul)
                operations.append(following)
                pr_calc.append(following)
                print(f"État actuel : {operations}")
            else:
                print("J'ai pas été clair, apprends à lire.")

    except ValueError:
        print("Erreur : entre des nombres et des opérateurs valides.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro détectée.")

# Menu for the calculator
def calculator_menu():
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
        elif choice == '2':  # Read history
            read_history_log()
        elif choice == '3':  # Simple calculation
            try:
                nb1 = float(input("Enter your first number: "))
                ope = input("Enter an operator (+, -, *, /): ")
                nb2 = float(input("Enter your second number: "))
                result = calcul_long(ope, nb1, nb2)
                print(f"Result: {result}")
            except ValueError:
                print("Erreur : entrez des nombres valides.")
            except ZeroDivisionError:
                print("Erreur : division par zéro.")
        elif choice == '4':  # Compound calculation
            compound_calculation()
        else:
            print("Invalid choice! Please enter a valid option.")

# Entry point
if __name__ == "__main__":
    calculator_menu()