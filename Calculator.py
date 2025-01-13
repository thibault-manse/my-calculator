flag = 0

try :
    nb1 = int(input("Rentrez votre 1er nombre : "))
except ValueError:
    print("Rentrez un nombre entier s'il vous plait")

while flag == 0:
    try :
        ope = int(input("Choisissez un opérateur : \n 1 : + \n 2 : - \n 3 : x \n 4 : / \n 5 : % \n 6 : puissance \n 7 : racine \n 8 div. euclidienne \n"))
    except ValueError:
        print("Rentrez un nombre entier s'il vous plait")
    if ope < 0 or ope > 8:
        print("Choix non valide")
    else :
        flag = 1

if ope != 7:
    try :
        nb2 = int(input("Rentrez votre 2eme nombre : "))
    except ValueError:
        print("Rentrez un nombre entier s'il vous plait")

if ope == 1:
    print(nb1, "+", nb2, "=", nb1 + nb2)

if ope == 2:
    print(nb1, "-", nb2, "=", nb1 - nb2)

if ope == 3:
    print(nb1, "x", nb2, "=", nb1 * nb2)

if ope == 4:
    print(nb1, "/", nb2, "=", nb1 / nb2)

if ope == 5:
    print(nb1, "%", nb2, "=", nb1 % nb2)

if ope == 6:
    print(nb1, "^", nb2, "=", nb1 ** nb2)

if ope == 7:
    print("Racine de ", nb1, "=", nb1 ** 0.5)

if ope == 8:
    print(nb1, "//", nb2, "=", nb1 // nb2)