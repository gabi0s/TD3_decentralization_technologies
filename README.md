# Projet de Prédiction avec Modèles Multi-Agent et Mécanisme de Consensus

Ce projet permet d'entraîner un modèle Random Forest et de mettre en place une API qui effectue des prédictions. Ensuite, il agrège les prédictions de plusieurs modèles en utilisant un mécanisme de consensus.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [ngrok](https://ngrok.com/download) (utilisé pour créer un tunnel HTTP sécurisé entre votre API et un lien accessible depuis l'extérieur)

### 1. Cloner le projet

Clonez ce projet en utilisant Git :

```bash
git clone https://github.com/votre-utilisateur/nom-du-repository.git
cd nom-du-repository
```

### 1. Lancer le 1er fichier
Lancez le premier fichier pour entraîner un modèle de prédiction (Random Forest) et créer une API qui écoute sur le port 5000 :
```bash
python app.py
```
Ce fichier entraîne le modèle RandomForestClassifier sur le dataset Iris et expose une API Flask sur http://localhost:5000. Vous pouvez accéder à cette API pour faire des prédictions.


### 2. Lancer le 2eme fichier
Une fois que l'API est en cours d'exécution et que ngrok a généré un lien public, lancez le deuxième fichier pour agréger les prédictions de plusieurs modèles en utilisant l'URL publique fournie par ngrok. Le deuxième fichier calcule la moyenne des prédictions de plusieurs modèles en utilisant les requêtes envoyées à l'API.
```bash
python app_ngrokF.py
```

### 3. Mécanisme de Consensus
Le fichier app_ngrokF.py implémente un mécanisme de consensus pour agréger les prédictions de plusieurs modèles. Les prédictions sont pondérées en fonction de la précision de chaque modèle, et un système de slashing est utilisé pour pénaliser les modèles inexactes. Ce processus permet de donner plus de poids aux modèles fiables et d'améliorer la performance globale.
