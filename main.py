"""
fonction pour l'historique
"""
# Fonction pour écrire l'historique dans un fichier log
def enregistrer_historique_log(historique):
    with open('historique_calculs.log', 'a') as fichier_log:
        for calcul in historique:
            fichier_log.write(f"{calcul['num1']} {calcul['operation']} {calcul['num2']} = {calcul['resultat']}\n")
        fichier_log.write("=== Fin d'historique ===\n")

# Fonction pour lire l'historique du fichier log
def lire_historique_log():
    try:
        with open('historique_calculs.log', 'r') as fichier_log:
            contenu = fichier_log.read()
            print("\n=== Contenu du fichier Log ===")
            print(contenu)
    except FileNotFoundError:
        print("Le fichier Log n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Log : {e}")

# Fonction pour effacer l'historique du fichier log
def effacer_historique_log():
    try:
        with open('historique_calculs.log', 'w') as fichier_log:
            pass  # Écrire rien pour effacer le contenu
        print("\nL'historique a été effacé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'historique : {e}")

# Liste pour enregistrer les calculs
historique = []

"""
Fonctions des calculs et Calculatrice
"""

# Fonctions des calculs
def addition(num1, num2):
    return num1 + num2

def soustraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Erreur: division par zéro"
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def racine_carree(num1):
    if num1 < 0:
        return "Erreur: impossible de calculer la racine carrée d'un nombre négatif"
    return num1 ** 0.5

# Initialiser 'resultat' avant la boucle
resultat = None

# Boucle de la Calculatrice
while True:
    print("\n=== CALCULATRICE ===")  # Titre clair
    print("\nOption de l'historique :")
    print("1. Voir l'historique")
    print("2. Effacer l'historique")
    print("3. Faire un calcul")
    choix_historique = input("Choisissez une option (1-lire/2-effacer/3-Faire un calcul) : ")

    if choix_historique == "1":
        lire_historique_log()
        continue
    elif choix_historique == "2":
        effacer_historique_log()
        continue
    elif choix_historique == "3":
        pass
    else:
        print("Option invalide. Veuillez choisir 1, 2 ou 3")
        continue

    try:
        # Demander à l'utilisateur s'il veut continuer avec un résultat précédent
        if resultat is not None:
            while True:
                continuer = input(f"Votre dernier résultat était {resultat}. Voulez-vous l'utiliser pour le prochain calcul ? (o/n) : ").lower().strip()
                if continuer in ["oui", "o"]:
                    num1 = resultat
                    break
                elif continuer in ["non", "n"]:
                    while True:
                        try:
                            num1 = float(input("Entrez le premier nombre : "))
                            break
                        except ValueError:
                            print("Erreur : Veuillez entrer un nombre valide.")
                    break
                else:
                    print("Erreur : Veuillez entrer 'oui', 'o', 'non', ou 'n'.")
        else:
            while True:
                try:
                    num1 = float(input("Entrez le premier nombre : "))
                    break
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide.")

        # Boucle pour demander et valider le second nombre
        while True:
            try:
                num2 = float(input("Entrez le second nombre : "))
                break
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide pour le second nombre.")

        # Boucle pour demande et valider l'opération
        while True:
            operateur = input("Entrez une opération (+, -, *, /) : ")
            if operateur in ["+", "-", "*", "/"]:
                break
            else:
                print("Erreur: Veuillez entrer un opérateur valide")

    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide pour le premier nombre.")
        continue

    # Exécuter l'opération choisie
    if operateur == "+":
        resultat = addition(num1, num2)
    elif operateur == "-":
        resultat = soustraction(num1, num2)
    elif operateur == "*":
        resultat = multiplication(num1, num2)
    elif operateur == "/":
        resultat = division(num1, num2)
   
    

    # Vérifier si le résultat est un entier
    if isinstance(resultat, float) and resultat.is_integer():
        resultat = int(resultat)

    print(f"Résultat : {resultat}")

<<<<<<< HEAD
=======
    """
    Ajout calcul historique et enregistrement log
    """

    # Ajouter le calcul à l'historique
>>>>>>> c5b4272b51e7bc5c7b465804840ff22c67fb0b8e
    historique.append({
        'num1': num1,
        'operation': operateur,
        'num2': num2,
        'resultat': resultat
    })

    enregistrer_historique_log(historique)

<<<<<<< HEAD
    choix = input("\nVoulez-vous effectuer un autre calcul ? (oui/non) : ").lower().strip()
=======
    """
    Boucles pour multicalculs
    """

    # Boucle pour plusieurs calculs
    choix = input("\nVoulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
>>>>>>> c5b4272b51e7bc5c7b465804840ff22c67fb0b8e
    if choix not in ["oui", "o"]:
        print("Au revoir !")
        break


# Appel de la fonction pour afficher l'historique log
lire_historique_log()
