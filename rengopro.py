# -*- coding: utf-8 -*-

import os
import sys

# Chemin du dossier contenant le script
dossier = sys.argv[1]
# Bidouille puir supprimer le " importé du batch sans raison apparente
dossier = dossier[:-1]


# Parcourez tous les fichiers du dossier
for nom_fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, nom_fichier)
    
    # Vérifiez si le fichier est un fichier .mp4 et suit le format "AAXXAAAA.mp4"
    if os.path.isfile(chemin_fichier)   and (nom_fichier.startswith("GX") or nom_fichier.startswith("GH")) and nom_fichier.endswith(".MP4") and len(nom_fichier) == 12:
        nouveau_nom = nom_fichier[0:2] + nom_fichier[4:8] + "-" + nom_fichier[2:4] + ".MP4"
        nouveau_chemin = os.path.join(dossier, nouveau_nom)
        os.rename(chemin_fichier, nouveau_chemin)
        print(f"Le fichier {nom_fichier} a été renommé en {nouveau_nom}")