def calcul(expression):
    def priorite_operateur(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/', ):
            return 2
        return 0

    def petite_libellule(a, b, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b


    '''La méthode .isdigit() en py, est utilisé pour vérifier si tout les caractère d'une chaine sont bien des chiffres. Elle retourne (true) si tous les caractères de la chaine sont des chiffres et qu'il y a au moins un caractère, sinon dans le cas contraire elle retourne (false).'''

    def soleil_expression(expression):
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
                    values.append(petite_libellule(val1, val2, op))
                ops.pop()
            else:
                while (len(ops) != 0 and priorite_operateur(ops[-1]) >= priorite_operateur(expression[i])):
                    val2 = values.pop()
                    val1 = values.pop()
                    op = ops.pop()
                    values.append(petite_libellule(val1, val2, op))
                ops.append(expression[i])
            i += 1

        ''' .pop c'est une méthode utilisé en Py, c'est une fonction de la classe list qui permet de supprimer un élément d'une liste et de renvoyer la valeur de l'élément supprimé. Elle peut prendre en compteun argument optionnel, qui est l'index de l'élément à supprimer.'''

        while len(ops) != 0:
            val2 = values.pop()
            val1 = values.pop()
            op = ops.pop()
            values.append(petite_libellule(val1, val2, op))

        return values[-1]

    return soleil_expression(expression)

def main():
    print("Bienvenue dans notre super calculatrice !")
    print("Entrez une expression mathématique (ou appuyez sur Q pour quitter) :")

    while True:
        expression = input("> ")
        if expression.lower() == 'q':
            break
        try:
            resultat = calcul(expression)
            print(f"Le résultat de l'expression '{expression}' est : {resultat}")
        except Exception as e:
            print(f"Erreur lors du calcul : {e}")

    print("Merci d'avoir calculé avec nous ! On espère que vos chiffres ont eu la pêche. À bientôt !")


if __name__ == "__main__":
    main()




