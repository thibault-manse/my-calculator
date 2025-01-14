from historique import Historique

class Calculatrice:
    """
    Classe principale pour effectuer des calculs.
    """

    def __init__(self):
        """
        Initialise une instance de la classe Calculatrice.

        Attributs :
        -----------
            Une liste vide qui stocke l'historique des calculs.
        historique_manager : Historique
            Une instance de la classe Historique qui gère les enregistrements et la lecture de l'historique.
        resultat : None
            Initialise le résultat à None, indiquant qu'aucun calcul n'a été effectué au départ.
        """
        self.historique = []  # Liste vide pour stocker l'historique des calculs
        self.historique_manager = Historique()  # Gestionnaire pour l'historique (objet de la classe Historique)
        self.resultat = None  # Aucun résultat initial, il sera mis à jour après chaque calcul

    def addition(self, num1, num2):
        return num1 + num2

    def soustraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Erreur: division par zero"  # Message d'erreur si on tente une division par zéro
        return num1 / num2

    def demander_nombre(self, prompt):
        """
        Demande à l'utilisateur d'entrer un nombre et valide l'entrée.
        """
        while True:
            try:
                return float(input(prompt))  # Demande un nombre et le convertit en float
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide.")  # Gestion des erreurs de type

    def demander_operation(self):
        while True:
            operateur = input("Entrez une opération (+, -, *, /) : ")
            if operateur in ("+", "-", "*", "/"):
                return operateur  # Retourne l'opérateur si valide
            print("Erreur: Veuillez entrer un opérateur valide.")

    def executer_calcul(self, num1, num2, operateur):
        """
        Exécute l'opération choisie avec num1 et num2 en fonction de l'opérateur.
        """
        if operateur == "+":
            return self.addition(num1, num2)
        elif operateur == "-":
            return self.soustraction(num1, num2)
        elif operateur == "*":
            return self.multiplication(num1, num2)
        elif operateur == "/":
            return self.division(num1, num2)

    def ajouter_historique(self, num1, operateur, num2, resultat):
        """
        Ajoute le calcul effectué et son résultat à l'historique.
        """
        self.historique.append({
            'num1': num1,
            'operation': operateur,
            'num2': num2,
            'resultat': resultat
        })

    def menu_historique(self):
        """
        Affiche les options relatives à l'historique des calculs et gère les choix de l'utilisateur.
        """
        print("\nOption de l'historique :")
        print("1. Voir l'historique")
        print("2. Effacer l'historique")
        print("3. Faire un calcul")
        choix_historique = input("Choisissez une option (1-lire/2-effacer/3-Calculer) : ")
        if choix_historique == "1":
            self.historique_manager.lire()
            return True  # Continuer après avoir vu l'historique
        elif choix_historique == "2":
            self.historique_manager.effacer()
            return True  # Continuer après avoir effacé l'historique
        elif choix_historique == "3":
            return False  # Aller faire un calcul, en sortant du menu
        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3")
            return True  # Retourner au menu si l'option est invalide

    def run(self):
        """
        Exécute la calculatrice en boucle.

        Permet à l'utilisateur de faire des calculs, de gérer l'historique et de répéter les calculs
        tant qu'il le souhaite.
        """
        while True:
            print("\n=== CALCULATRICE ===")

            # Menu historique (si l'utilisateur le souhaite)
            if not self.menu_historique():
                continue

            # Si un résultat existe déjà, on demande à l'utilisateur s'il veut l'utiliser
            if self.resultat is not None:
                utiliser_resultat = input(f"Votre dernier résultat était {self.resultat}. Voulez-vous l'utiliser ? (o/n) : ").lower()
                if utiliser_resultat == "o":
                    num1 = self.resultat
                else:
                    num1 = self.demander_nombre("Entrez le premier nombre : ")
            else:
                num1 = self.demander_nombre("Entrez le premier nombre : ")

            operateur = self.demander_operation()
            num2 = self.demander_nombre("Entrez le second nombre : ")

            # Vérification et conversion de num1 et num2 en int si possible
            if isinstance(num1, (int, float)) and num1 == int(num1):
                num1 = int(num1)

            if isinstance(num2, (int, float)) and num2 == int(num2):
                num2 = int(num2)

            # Vérification et conversion du résultat en int si possible
            if isinstance(self.resultat, (int, float)) and self.resultat == int(self.resultat):
                self.resultat = int(self.resultat)

            # Calcul du résultat
            self.resultat = self.executer_calcul(num1, num2, operateur)
            print(f"Résultat : {self.resultat}")

            # Ajout du calcul à l'historique
            self.ajouter_historique(num1, operateur, num2, self.resultat)
            self.historique_manager.enregistrer(self.historique)

            # Demande si l'utilisateur veut effectuer un autre calcul
            continuer = input("\nVoulez-vous effectuer un autre calcul ? (o/n) : ").lower()
            if continuer not in ["o", "oui"]:
                print("Au revoir !")
                break
