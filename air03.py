import sys

def afficher_valeur_pas_en_double():
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] not in sys.argv[:i] and sys.argv[i] not in sys.argv[i+1:]:
            print(sys.argv[i])
            i = i + 1

        else:
            i = i + 1



afficher_valeur_pas_en_double()