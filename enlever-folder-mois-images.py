import os
import shutil
from datetime import datetime
# déplace les images des sous-dossiers mensuels vers leur dossier parent annuel
def deplacer_images_vers_parent(dossier_racine):
    # Extensions d'images courantes
    extensions_images = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    # Compteurs pour le rapport
    fichiers_deplaces = 0
    dossiers_supprimes = 0
    
    # Parcourir tous les dossiers
    for dossier_actuel, sous_dossiers, fichiers in os.walk(dossier_racine, topdown=False):
        # Vérifier si le dossier actuel est un dossier mensuel (01-12)
        dossier_base = os.path.basename(dossier_actuel)
        dossier_parent = os.path.dirname(dossier_actuel)
        
        if dossier_base.isdigit() and 1 <= int(dossier_base) <= 12:
            # Déplacer tous les fichiers images vers le dossier parent
            for fichier in fichiers:
                if fichier.lower().endswith(extensions_images):
                    source = os.path.join(dossier_actuel, fichier)
                    destination = os.path.join(dossier_parent, fichier)
                    
                    # Gérer les doublons
                    if os.path.exists(destination):
                        nom_base, extension = os.path.splitext(fichier)
                        i = 1
                        while os.path.exists(destination):
                            nouveau_nom = f"{nom_base}_{i}{extension}"
                            destination = os.path.join(dossier_parent, nouveau_nom)
                            i += 1
                    
                    try:
                        shutil.move(source, destination)
                        print(f"Déplacé : {source} -> {destination}")
                        fichiers_deplaces += 1
                    except Exception as e:
                        print(f"Erreur lors du déplacement de {source}: {e}")
            
            # Vérifier si le dossier est vide et le supprimer
            if not os.listdir(dossier_actuel):
                try:
                    os.rmdir(dossier_actuel)
                    print(f"Dossier supprimé : {dossier_actuel}")
                    dossiers_supprimes += 1
                except Exception as e:
                    print(f"Erreur lors de la suppression du dossier {dossier_actuel}: {e}")
    
    return fichiers_deplaces, dossiers_supprimes

if __name__ == "__main__":
    # Demander le chemin du dossier racine
    dossier_racine = input("Entrez le chemin du dossier à analyser : ")
    
    # Vérifier si le dossier existe
    if not os.path.exists(dossier_racine):
        print("Le dossier spécifié n'existe pas.")
    else:
        # Confirmation avant de procéder
        confirmation = input("Êtes-vous sûr de vouloir déplacer les images ? (oui/non) : ")
        
        if confirmation.lower() == 'oui':
            fichiers_deplaces, dossiers_supprimes = deplacer_images_vers_parent(dossier_racine)
            print(f"\nOpération terminée.")
            print(f"Fichiers déplacés : {fichiers_deplaces}")
            print(f"Dossiers supprimés : {dossiers_supprimes}")
        else:
            print("Opération annulée.")
