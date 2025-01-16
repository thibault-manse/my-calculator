def calculate(a, b, operation):
    """Perform the calculation based on the operation."""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Cannot divide by zero.")
            return None
    else:
        print("Invalid operation! Please use +, -, *, or /. Try again.")
        return None

def save_history(history):
    """Save the history."""
    with open("history.txt", "w") as file:
        for entry in history:
            file.write(entry + "\n")
    print("History saved to 'history.txt'.")

def read_history():
    """Read the history and return it as a list of entries."""
    try:
        with open("history.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("No history found.")
        return []

def clear_history():
    """Clear the history."""
    try:
        with open("history.txt", "w") as file:
            pass  # This effectively clears the content of the file
        print("History cleared.")
    except FileNotFoundError:
        print("No history found to clear.")

def calculator_menu():
    history = []  # List to keep the calculation history

    while True:
        print("\n=== Calculator Menu: ===")
        print("\n1. Clear history")
        print("2. Read history")
        print("3. Save history")
        print("4. Calculate")
        print("5. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '5':
            print("Thank you for using the calculator! Bye.")
            break
        elif choice == '1':  # Clear history 
            clear_history()
            print("History cleared.")
        elif choice == '2':  # Read history
            read_history()
            print("Read history")
        elif choice == '3':  # Save history
            save_history(history)

        elif choice == '4': # Calculate
            calculate()
            print("Calculate")

        else:
            print("Invalid choice! Please enter a valid option.")
            continue

        # If the choice is 1, 2, or 3, no further input is required.
        if choice in ['1', '2', '3']:
            continue

        # Ask for two numbers for other operations (integers only)
        a = int(input("Enter the first number (integer): "))
        b = int(input("Enter the second number (integer): "))

        # Perform the calculation using the new calculate function
        operation = input("Enter operation (+, -, *, /): ")
        result = calculate(a, b, operation)

        if result is not None:
            # Display the result and add it to the history
            print(f"Result: {result}")
            history.append(f"{a} {operation} {b} = {result}")

if __name__ == "__main__":
    calculator_menu()
