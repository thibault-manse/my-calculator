def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error: Division by zero!")
    return a / b

def afficher_historique(historique):
    if len(historique) == 0:
        print("The history is empty.")
    else:
        for index, operation in enumerate(historique, 1):
            print(f"{index}. {operation}")

def calculatrice():
    historique = []
    
    '''menu to choose an option and perform the operation'''
    #menu
    while True:
        print("\nCalculator:")
        print("1. Add")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Show history")
        print("6. Clear history")
        print("7. Exit")
        
        choix = input("Choose an option (1-7): ")
        
        if choix == '7':
            print("Thank you for using the calculator! Byebye.")
            break
        elif choix == '5':
            afficher_historique(historique)
        elif choix == '6':
            historique.clear()
            print("History reset.")
        elif choix in ['1', '2', '3', '4']:
            try:

                '''To choose numbers using the float class'''
                # Ask for inputs
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                
                '''these are the calculations to perform depending on the chosen operation'''
                # Calculate based on the chosen option
                if choix == '1':
                    result = add(a, b)
                    operation = f"{a} + {b} = {result}"
                elif choix == '2':
                    result = subtraction(a, b)
                    operation = f"{a} - {b} = {result}"
                elif choix == '3':
                    result = multiplication(a, b)
                    operation = f"{a} * {b} = {result}"
                elif choix == '4':
                    result = divide(a, b)
                    operation = f"{a} / {b} = {result}"
                
                print(f"Result: {result}")
                
                '''this is to display the history as requested by the user'''
                # Add to history
                historique.append(operation)
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        else:
            print("Invalid choice! Please enter a valid option. Try again, little goat of the meadows.")

if __name__ == "__main__":
    calculatrice()

