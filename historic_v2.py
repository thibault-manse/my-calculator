# List to store the history of calculations
history = []

def calculate():
    operation = input('''
Please type in the operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        result = number_1 + number_2
        print('{} + {} = {}'.format(number_1, number_2, result))
        
    elif operation == '-':
        result = number_1 - number_2
        print('{} - {} = {}'.format(number_1, number_2, result))
        
    elif operation == '*':
        result = number_1 * number_2
        print('{} * {} = {}'.format(number_1, number_2, result))
        
    elif operation == '/':
        if number_2 != 0:
            result = number_1 / number_2
            print('{} / {} = {}'.format(number_1, number_2, result))
        else:
            print("Cannot divide by zero.")
            result = None
    else:
        print('You have not typed a valid operator, please run the program again, little goat.')
        result = None

    # If the calculation was successful, add to history
    if result is not None:
        history.append(f'{number_1} {operation} {number_2} = {result}')
    
    # Display the history after each calculation
    print("\nHistory:")
    for entry in history:
        print(entry)

    # Ask the user if they want to delete the history
    delete_history = input('Do you want to delete the history? Y for YES or N for NO: ')
    if delete_history.upper() == 'Y': #The upper() method, is used to convert a string to uppercase letters.
        clear_history()
    else:
        # Call the 'again()' function to ask if the user wants to calculate again
        again()

def clear_history():
    # Clear the history list
    history.clear()
    print("History has been deleted.")

def again():
    calc_again = input(''' 
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()

