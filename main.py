"""
Function for the history
"""
# Function to write the history to a log file
def save_history_log(history):
    with open('calculation_history.log', 'a') as log_file:
        for calculation in history:
            log_file.write(f"{calculation['num1']} {calculation['operation']} {calculation['num2']} = {calculation['result']}\n")
        log_file.write("=== End of history ===\n")

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

# List to store the calculations
history = []

"""
Functions for calculations and Calculator
"""

# Calculation functions
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: division by zero"
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def square_root(num1):
    if num1 < 0:
        return "Error: cannot calculate the square root of a negative number"
    return num1 ** 0.5

# Initialize 'result' before the loop
result = None

# Calculator loop
while True:
    print("\n=== CALCULATOR ===")  # Clear title
    print("\nHistory options:")
    print("1. View history")
    print("2. Clear history")
    print("3. Make a calculation")
    history_choice = input("Choose an option (1-view/2-clear/3-make a calculation): ")

    if history_choice == "1":
        read_history_log()
        continue
    elif history_choice == "2":
        clear_history_log()
        continue
    elif history_choice == "3":
        pass
    else:
        print("Invalid option. Please choose 1, 2, or 3.")
        continue

    try:
        # Ask the user if they want to continue with a previous result
        if result is not None:
            while True:
                continue_choice = input(f"Your last result was {result}. Do you want to use it for the next calculation? (y/n): ").lower().strip()
                if continue_choice in ["yes", "y"]:
                    num1 = result
                    break
                elif continue_choice in ["no", "n"]:
                    while True:
                        try:
                            num1 = float(input("Enter the first number: "))
                            break
                        except ValueError:
                            print("Error: Please enter a valid number.")
                    break
                else:
                    print("Error: Please enter 'yes', 'y', 'no', or 'n'.")
        else:
            while True:
                try:
                    num1 = float(input("Enter the first number: "))
                    break
                except ValueError:
                    print("Error: Please enter a valid number.")

        # Loop to ask and validate the second number
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Error: Please enter a valid number for the second number.")

        # Loop to ask and validate the operation
        while True:
            operator = input("Enter an operation (+, -, *, /): ")
            if operator in ["+", "-", "*", "/"]:
                break
            else:
                print("Error: Please enter a valid operator")

    except ValueError:
        print("Error: Please enter a valid number for the first number.")
        continue

    # Perform the chosen operation
    if operator == "+":
        result = addition(num1, num2)
    elif operator == "-":
        result = subtraction(num1, num2)
    elif operator == "*":
        result = multiplication(num1, num2)
    elif operator == "/":
        result = division(num1, num2)

    # Check if the result is an integer
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    print(f"Result: {result}")

    """
    Add calculation to history and save log
    """

    # Add the calculation to the history
    history.append({
        'num1': num1,
        'operation': operator,
        'num2': num2,
        'result': result
    })

    save_history_log(history)

    """
    Loops for multiple calculations
    """

    # Loop for multiple calculations
    choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if choice not in ["yes", "y"]:
        print("Goodbye!")
        break


# Call the function to display the history log
read_history_log()
