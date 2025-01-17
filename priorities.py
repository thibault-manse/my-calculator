def calculate(expression):
    def operator_priority(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operation(a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b

    '''The .isdigit() method in Python is used to check if all characters in a string are digits. 
    It returns (True) if all characters in the string are digits and there is at least one character, 
    otherwise, it returns (False).'''

    def analyze_expression(expression):
        values = []
        ops = []
        i = 0

        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i] == '(':
                ops.append(expression[i])
            elif expression[i].isdigit():
                val = 0
                while i < len(expression) and expression[i].isdigit():
                    val = val * 10 + int(expression[i])
                    i += 1
                values.append(val)
                i -= 1
            elif expression[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(apply_operation(val1, val2, op))
                ops.pop()
            else:
                while (len(ops) != 0 and operator_priority(ops[-1]) >= operator_priority(expression[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(apply_operation(val1, val2, op))
                ops.append(expression[i])
            i += 1

        '''.pop is a method used in py, it's a function of the list class that removes an element from a list 
        and returns the value of the removed element. It can take an optional argument, which is the index of the element to remove.'''

        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(apply_operation(val1, val2, op))

        return values[-1]

    return analyze_expression(expression)

def main():
    print("Welcome to our super calculator!")
    print("Enter a mathematical expression (or press Q to quit):")

    while True:
        expression = input("> ")
        if expression.lower() == 'q':
            break
        try:
            result = calculate(expression)
            print(f"The result of the expression '{expression}' is: {result}")
        except Exception as e:
            print(f"Error during calculation: {e}")

    print("Thank you for calculating with us! We hope your numbers were full of energy. See you soon!")

if __name__ == "__main__":
    main()
