import json

"""
fonction json pour enregistrer l'historique
"""

# Fonction pour enregistrer l'historique des calculs dans un fichier
def enregistrer_historique(historique):
    # Ouvre le fichier en mode écriture (il sera créé s'il n'existe pas)
    with open('historique_calculs.json', 'w') as f:
        # Enregistre l'historique dans le fichier JSON
        json.dump(historique, f, indent=4)

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
    Enregistrement de l'historique
    """

    # Enregistrer l'historique dans un fichier JSON
    enregistrer_historique(historique)

    # Boucle pour plusieurs calculs
    choix = input("\nVoulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
    if choix not in ["oui", "o"]:
        print("Au revoir !")
        break  # Quitter la boucle
