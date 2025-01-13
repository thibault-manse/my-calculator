

"""
fonction log pour enregistrer l'historique
"""



#fonction pour ecrire l'historique dans un fichier log
def enregistrer_historique_log(historique):
    #ouvre le fichier log en mode ajout
    with open('historique_calculs.log', 'a') as fichier_log:
        #parcourir chaque calcu dans l'historique
        for calcul in historique:
            #formater et écrire chaque opération dans le log
            fichier_log.write(f"{calcul['num1']} {calcul['operation']} {calcul['num2']} = {calcul['resultat']}\n")
            fichier_log.write("=== Fin de session ===\n")

# Fonction pour lire l'historique depuis le fichier log
def lire_historique_log():
    try:
        # Ouvrir le fichier log en mode lecture ('r')
        with open('historique_calculs.log', 'r') as fichier_log:
            # Lire tout le contenu du fichier
            contenu = fichier_log.read()
            print("\n=== Contenu du fichier Log ===")
            print(contenu)
    except FileNotFoundError:
        print("Le fichier Log n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Log : {e}")


# Liste où on va rajouter les calculs
historique = []

"""
fonctions des calculs
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

# Initialiser 'resultat' avant la boucle
resultat = None

# Boucle de la Calculatrice
while True:
    print("\n=== CALCULATRICE ===")  # Titre clair
    try:
        # Demander à l'utilisateur s'il veut continuer avec un résultat précédent
        if resultat is not None:  # Vérifier si 'resultat' a été défini (différent de None)
            continuer = input(f"Votre dernier résultat était {resultat}. Voulez-vous l'utiliser pour le prochain calcul ? (oui/non) : ").lower()
            if continuer in ['oui', 'o']:
                num1 = resultat  # Utiliser le dernier résultat comme premier nombre
            elif continuer in ['non', 'n']:
                num1 = float(input("Entrez le premier nombre : "))  # Demander un nouveau premier nombre
        else:
            num1 = float(input("Entrez le premier nombre : "))  # Si c'est le premier calcul, demander le premier nombre

        # Boucle pour demander et valider le second nombre
        while True:
            try:
                num2 = float(input("Entrez le second nombre : "))
                break  # Sortir de la boucle si l'entrée est valide
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide pour le second nombre.")

        # Boucle pour demande et valider l'opération
        while True:
            operateur = input("Entrez une opération (+, -, *, /) : ")
            if operateur in ("+", "-", "*", "/"):
                break
            else:
                print("Erreur: Veuillez entrez un opérateur valide")

    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide pour le premier nombre.")
        continue  # Recommencer depuis le début

    # Vérification et conversion num1 et num2
    if isinstance(num1, (int, float)) and num1 == int(num1):
        num1 = int(num1)

    if isinstance(num2, (int, float)) and num2 == int(num2):
        num2 = int(num2)

    # Exécuter l'opération choisie
    if operateur == "+":
        resultat = addition(num1, num2)
    elif operateur == "-":
        resultat = soustraction(num1, num2)
    elif operateur == "*":
        resultat = multiplication(num1, num2)
    elif operateur == "/":
        resultat = division(num1, num2)
    else:
        print("Erreur : Opération invalide")
        continue  # Recommencer depuis le début

    # Vérifier si le résultat est un entier ou un flottant
    if isinstance(resultat, (int, float)) and resultat == int(resultat):
        resultat = int(resultat)

    # Afficher le résultat
    print(f"{num1} {operateur} {num2} = {resultat}")

    # Ajouter le calcul à l'historique
    historique.append({
        'num1': num1,
        'operation': operateur,
        'num2': num2,
        'resultat': resultat
    })

    """
    Enregistrement de l'historique log
    """

    # Enregistrer l'historique dans un fichier JSON
    # enregistrer_historique_json(historique)

    #enregistrer l'historique dans un fichier log
    enregistrer_historique_log(historique)

    # Boucle pour plusieurs calculs
    choix = input("\nVoulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
    if choix not in ["oui", "o"]:
        print("Au revoir !")
        break  # Quitter la boucle

# Appel de la fonction pour afficher l'historique log
lire_historique_log()