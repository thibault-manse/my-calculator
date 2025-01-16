flag = 0 #switch

try :
    nb1 = int(input("Rentrez votre 1er nombre : ")) #fisrt number to calculate
except ValueError:
    print("Rentrez un nombre entier s'il vous plait")

def choix(flag):
    #choice operator
    while flag == 0:
        try :
            ope = int(input("Choisissez un opérateur : \n 1 : + \n 2 : - \n 3 : x \n 4 : / \n 5 : % \n 6 : puissance \n 7 : racine \n 8 : div. euclidienne \n"))
        except ValueError:
            print("Rentrez un nombre entier s'il vous plait")
        if ope < 0 or ope > 8:
            print("Choix non valide")
        else :
            flag = 1

    #if operator is square root
    if ope != 7:
        try :
            nb2 = int(input("Rentrez votre 2eme nombre : "))
        except ValueError:
            print("Rentrez un nombre entier s'il vous plait")

    flag = 0
    liste = (nb2, ope, flag) #tuple with number2, the operator and switch
    return liste

result = 0
flag2 = 0

def calcul_long(operateur, a, b):
    

try:
    calcc = float(input("Entrez le premier nombre : "))
    operations = [calcc]  

    while True:
        
        calcul = input("T'as le choix entre ces calculs : '+', '-', '*', '/' ou tape 'fin' si t'en peux plus : ")
        if calcul == "fin":
            # Résolution des calculs en respectant les priorités
            while len(operations) > 1:
                # Recherche des opérations prioritaires 
                idx = next((i for i in range(1, len(operations), 2) if operations[i] in "*/"), None)
                if idx is None:  
                    idx = 1  
                
                # Applique l'opération
                res = calcul_long(operations[idx], operations[idx - 1], operations[idx + 1])
                # Remplace les éléments par le résultat
                operations[idx - 1:idx + 2] = [res]

            print(f"Et le résultat est : {operations[0]}")
            break

        if calcul in {"+", "-", "*", "/"}:
            following = float(input("Entre ton nombre : "))
            operations.append(calcul)  
            operations.append(following)  
            print(f"État actuel : {operations}")
        else:
            print("J'ai pas été clair débile, apprends à lire.")

except ValueError:
    print("Erreur: entre des nombres et des opérateurs valides.")
except ZeroDivisionError:
    print("Erreur : Division par zéro détectée.")

def calc(nb1, nb2, ope, result, flag2, flag): #fonction calculator with choise to continue or not
    if flag2 == 0: #if it's the first calculation
        if ope == 1:
            result = nb1 + nb2
            print(nb1, "+", nb2, "=", result)
        if ope == 2:
            result = nb1 - nb2
            print(nb1, "-", nb2, "=", result)
        if ope == 3:
            result = nb1 * nb2
            print(nb1, "x", nb2, "=", result)
        if ope == 4:
            result = nb1 / nb2
            print(nb1, "/", nb2, "=", result)
        if ope == 5:
            result = nb1 % nb2
            print(nb1, "%", nb2, "=", result)
        if ope == 6:
            result = nb1 ** nb2
            print(nb1, "^", nb2, "=", result)
        if ope == 7:
            result = nb1 ** 0.5
            print("Racine de ", nb1, "=", result)
        if ope == 8:
            result = nb1 // nb2
            print(nb1, "//", nb2, "=", result)
        flag2 = 1

    elif flag2 == 1 : #if it's not the first calculation
        result_prev = result
        if ope == 1:
            result = result + nb2
            print(result_prev, "+", nb2, "=", result)
        if ope == 2:
            result = result - nb2
            print(result_prev, "-", nb2, "=", result)
        if ope == 3:
            result = result * nb2
            print(result_prev, "x", nb2, "=", result)
        if ope == 4:
            result = result / nb2
            print(result_prev, "/", nb2, "=", result)
        if ope == 5:
            result = result % nb2
            print(result_prev, "%", nb2, "=", result)
        if ope == 6:
            result = result ** nb2
            print(result_prev, "^", nb2, "=", result)
        if ope == 7:
            result = result ** 0.5
            print("Racine de ", result_prev, "=", result)
        if ope == 8:
            result = result // nb2
            print(result_prev, "//", nb2, "=", result)
    
    #choise to continue the calculation or not
    try :
        choise = str(input("Continuer le calcule ? (Y ou N) ")).upper()
    except ValueError :
        print("Valeur non valide")
    except choise != "Y" or choise != "N" :
        print("Rentrez une valeur valide (Y ou N)")
        
    if choise == "Y" :
        nb2, ope, flag= choix(flag)
        calc(nb1, nb2, ope, result, flag2, flag)
    elif choise == "N" :
        return 0
    
nb2, ope, flag = choix(flag)
calc(nb1, nb2, ope, result, flag2, flag)
