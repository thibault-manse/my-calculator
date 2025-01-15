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



# Call the function to display the history log
read_history_log()