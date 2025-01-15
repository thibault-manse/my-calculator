def choix():
    while True:
        try:
            ope = int(input(
                "Choisissez un opérateur : \n 1 : + \n 2 : - \n 3 : x \n 4 : / \n 5 : % \n 6 : puissance \n 7 : racine \n 8 : div. euclidienne \n"))
            if ope < 1 or ope > 8:
                print("Choix non valide. Veuillez choisir un nombre entre 1 et 8.")
            else:
                break
        except ValueError:
            print("Rentrez un nombre entier valide s'il vous plait.")

    nb2 = None
    if ope != 7:  # Pas besoin d'un deuxième nombre pour la racine carrée
        while True:
            try:
                nb2 = float(input("Rentrez votre 2ème nombre : "))
                break
            except ValueError:
                print("Rentrez un nombre valide s'il vous plait.")

    return nb2, ope


def calc():
    try:
        nb1 = float(input("Rentrez votre 1er nombre : "))
    except ValueError:
        print("Rentrez un nombre entier valide s'il vous plait.")
        return

    result = nb1
    while True:
        nb2, ope = choix()

        if ope == 1:
            result += nb2
            print(f"{result - nb2} + {nb2} = {result}")
        elif ope == 2:
            result -= nb2
            print(f"{result + nb2} - {nb2} = {result}")
        elif ope == 3:
            result *= nb2
            print(f"{result / nb2} x {nb2} = {result}")
        elif ope == 4:
            if nb2 == 0:
                print("Division par zéro non autorisée.")
                continue
            result /= nb2
            print(f"{result * nb2} / {nb2} = {result}")
        elif ope == 5:
            if nb2 == 0:
                print("Modulo par zéro non autorisé.")
                continue
            result %= nb2
            print(f"{result + nb2} % {nb2} = {result}")
        elif ope == 6:
            result **= nb2
            print(f"({result ** (1/nb2)}) ^ {nb2} = {result}")
        elif ope == 7:
            if result < 0:
                print(
                    "La racine carrée d'un nombre négatif n'est pas définie dans les nombres réels.")
                continue
            result = result ** 0.5
            print(f"Racine de {result ** 2} = {result}")
        elif ope == 8:
            if nb2 == 0:
                print("Division euclidienne par zéro non autorisée.")
                continue
            result //= nb2
            print(f"{result * nb2 + nb2 % result} // {nb2} = {result}")

        continuer = input(
            "Voulez-vous continuer le calcul ? (Y/N) : ").strip().upper()
        if continuer != "Y":
            print("Fin du calcul. Résultat final :", result)
            break


if __name__ == "__main__":
    calc()
