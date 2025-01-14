class Historique:
    """
    Classe pour gérer l'historique des calculs.

    Attributs :
    ----------
    log_file : str
        Chemin vers le fichier où l'historique des calculs est enregistré.

    3 méthodes :
    -----------
    - enregistrer: Enregistre les calculs dans le fichier log.
    - lire: Affiche le contenu du fichier log.
    - effacer: Vide le contenu du fichier log.
    """

    def __init__(self, log_file='historique_calculs.log'):
        """
        Initialise une instance de la classe Historique.

        Paramètres :
        ------------
        log_file : str
            Le chemin vers le fichier où l'historique des calculs sera enregistré. Par défaut, il est défini à 'historique_calculs.log'.
        """
        self.log_file = log_file  # Définit le fichier log dans lequel les calculs seront enregistrés.

    def enregistrer(self, historique):
        """
        Enregistre une liste de calculs dans le fichier log.
        Chaque calcul est un dictionnaire avec les clés : 'num1', 'operation', 'num2' et 'resultat'.
        Chaque calcul sera ajouté à la fin du fichier log.

        Paramètre :
        -----------
        historique : list
            Une liste de dictionnaires où chaque dictionnaire représente un calcul.
        """
        try:
            with open(self.log_file, 'a') as fichier_log:
                for calcul in historique:
                    # Enregistre chaque calcul au format lisible
                    fichier_log.write(f"{calcul['num1']} {calcul['operation']} {calcul['num2']} = {calcul['resultat']}\n")
                fichier_log.write("=== Fin d'historique ===\n")  # Indicateur de fin de l'historique
            print("Historique enregistré avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'enregistrement dans le fichier Log : {e}")

    def lire(self):
        """
        Lit et affiche le contenu du fichier log.

        Cette méthode essaie d'ouvrir le fichier log en lecture et d'afficher son contenu.
        Si le fichier n'existe pas, elle affiche un message d'erreur.
        """
        try:
            with open(self.log_file, 'r') as fichier_log:
                contenu = fichier_log.read()
                print("\n=== Contenu du fichier Log ===")
                print(contenu)
        except FileNotFoundError:
            print("Le fichier Log n'existe pas.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier Log : {e}")

    def effacer(self):
        """
        Efface le contenu du fichier log.

        Cette méthode vide le fichier log spécifié pour supprimer l'historique des calculs.
        """
        try:
            with open(self.log_file, 'w') as fichier_log:
                pass  # N'écrit rien pour vider le contenu du fichier
            print("\nL'historique a été effacé avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression de l'historique : {e}")
