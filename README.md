# my-calculator
# Calculatrice de Menu

## Installation

Pour utiliser la Calculatrice de Menu, vous devez avoir Python installé sur votre machine. Vous pouvez télécharger la dernière version de Python depuis le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/).

Une fois Python installé, vous pouvez télécharger le fichier `menuCalculator.py` et le sauvegarder à l'emplacement de votre choix.

## Utilisation

Pour exécuter la Calculatrice de Menu, ouvrez un terminal ou une invite de commande, naviguez jusqu'au répertoire où vous avez enregistré le fichier `menuCalculator.py`, puis exécutez la commande suivante :

```
python menuCalculator.py
```

### Cela démarrera le menu de la calculatrice, où vous pourrez choisir parmi les options suivantes :

1. Effacer l'historique
2. Lire l'historique
3. Calculer
4. Quitter

### La calculatrice prend en charge les opérations suivantes :

- Addition (+)
- Soustraction (-)
- Multiplication (x)
- Division (/)
- Modulo (%)
- Puissance (^)
- Racine carrée (√)
- Division euclidienne (//)

Vous pouvez choisir de travailler avec des entiers ou des nombres décimaux.

## API

### Le fichier `menuCalculator.py` fournit les fonctions suivantes :

- `save_history_log(nb1, nb2, ope, result)`: Sauvegarde l'historique des calculs dans un fichier JSON.
- `read_history_log()`: Lit l'historique des calculs depuis le fichier JSON et l'affiche.
- `clear_history_log()`: Supprime le fichier d'historique des calculs.
- `calculator_menu()`: Exécute le menu principal de la calculatrice.
- `operator(flag, int_and_float)`: Gère le choix de l'opérateur de l'utilisateur et le deuxième opérande.
- `calc(nb1, nb2, ope, result, flag3, flag, int_and_float)`: Effectue le calcul et sauvegarde le résultat.

## Contribution

Si vous trouvez des problèmes ou avez des suggestions d'améliorations, n'hésitez pas à ouvrir une nouvelle issue ou à soumettre une pull request sur le dépôt GitHub du projet.

## Tests

Pour tester la Calculatrice de Menu, vous pouvez exécuter le fichier `menuCalculator.py` et essayer les différentes fonctionnalités, telles que la réalisation de calculs mathématique, la sauvegarde et la lecture de l'historique, ainsi que l'effacement de l'historique grace à Json.
