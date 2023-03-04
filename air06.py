import sys



def supprimer_element_qui_ne_contient_pas_une_lettre(lst,char):
    i = 0
    while i < len(lst):
            if char.upper() in lst[i] or char.lower() in lst[i]:
                del lst[i]
            else:
                i = i + 1

    return lst



try:
    resultat = supprimer_element_qui_ne_contient_pas_une_lettre(sys.argv[1:-1], sys.argv[-1])
    for element in resultat:
        print(element, end = " ")


except IndexError:
    pass

except:
    print("Error")


