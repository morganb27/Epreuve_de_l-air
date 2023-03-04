import sys

def afficher_le_contenu_fichier(fichier):
    fichier = open(sys.argv[1], 'r')
    contenu = fichier.read()
    print(contenu)

afficher_le_contenu_fichier(sys.argv[1])