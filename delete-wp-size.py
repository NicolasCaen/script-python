import os
import re

def supprimer_images_wordpress(dossier_racine):
    # Motif pour détecter les images redimensionnées WordPress (-150x150, -300x300, etc.)
    pattern = re.compile(r'-\d+x\d+\.(jpg|jpeg|png|gif)$', re.IGNORECASE)
    
    # Nombre d'images supprimées
    compteur = 0
    
    # Parcourir tous les dossiers et sous-dossiers
    for dossier_actuel, sous_dossiers, fichiers in os.walk(dossier_racine):
        for fichier in fichiers:
            # Vérifier si le fichier correspond au motif WordPress
            if pattern.search(fichier):
                chemin_complet = os.path.join(dossier_actuel, fichier)
                try:
                    # Supprimer le fichier
                    os.remove(chemin_complet)
                    print(f"Supprimé : {chemin_complet}")
                    compteur += 1
                except Exception as e:
                    print(f"Erreur lors de la suppression de {chemin_complet}: {e}")
    
    return compteur

if __name__ == "__main__":
    # Demander le chemin du dossier racine
    dossier_racine = input("Entrez le chemin du dossier à analyser : ")
    
    # Vérifier si le dossier existe
    if not os.path.exists(dossier_racine):
        print("Le dossier spécifié n'existe pas.")
    else:
        # Confirmation avant suppression
        confirmation = input("Êtes-vous sûr de vouloir supprimer les images redimensionnées ? (oui/non) : ")
        
        if confirmation.lower() == 'oui':
            nombre_fichiers = supprimer_images_wordpress(dossier_racine)
            print(f"\nOpération terminée. {nombre_fichiers} fichiers ont été supprimés.")
        else:
            print("Opération annulée.")
