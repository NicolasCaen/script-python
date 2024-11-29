# Description des Scripts Python

## delete-wp-size.py

Ce script est conçu pour supprimer les images redimensionnées générées par WordPress. Il parcourt récursivement un dossier spécifié et supprime les fichiers d'image dont le nom se termine par un suffixe de type `-150x150`, `-300x300`, etc.

### Fonctionnalités
- Supprime les images redimensionnées automatiquement.
- Supporte les formats d'image : jpg, jpeg, png, gif.
- Affiche un rapport des fichiers supprimés.

### Utilisation
Exécutez le script et entrez le chemin du dossier à analyser lorsque vous y êtes invité.

## enlever-folder-mois-images.py

Ce script déplace les images des sous-dossiers mensuels (nommés de 01 à 12) vers leur dossier parent annuel. Il supprime également les dossiers mensuels une fois qu'ils sont vides.

### Fonctionnalités
- Déplace les images vers le dossier parent.
- Gère les doublons en renommant les fichiers si nécessaire.
- Supprime les dossiers mensuels vides.
- Supporte les formats d'image : jpg, jpeg, png, gif, webp.

### Utilisation
Exécutez le script et entrez le chemin du dossier à analyser lorsque vous y êtes invité.

### Remarques
- Assurez-vous de faire une sauvegarde de vos fichiers avant d'exécuter ces scripts, car les modifications sont irréversibles.
- Les scripts demandent une confirmation avant d'effectuer des modifications.
- Les chemins contenant des espaces doivent être correctement formatés (utilisez des guillemets ou échappez les espaces).

### Prérequis
- Python 3 doit être installé sur votre système.
- Les scripts utilisent uniquement des modules Python standards (os, shutil, re).
