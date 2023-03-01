import sys



def supprimer_caracteres_identiques_adjacents():
    i = 0
    str = sys.argv[1]

        while i < (len(str) - 1):
            if str[i] != str[i+1] and str[i] != " ":
                print(str[i], end = "")
                i = i + 1

            if str[i] == " ":
                print(" ", end="")

            else:
                i = i + 1

    print(str[-1], end = " ")

supprimer_caracteres_identiques_adjacents()