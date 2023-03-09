import sys

def supprimer_caracteres_identiques_adjacents():
    s = sys.argv[1]
    result = ""
    last_char = None

    for i in range(len(s)):
        if s[i] != last_char:
            result += s[i]
            last_char = s[i]

    return result

if len(sys.argv) < 2:
    print("Veuillez fournir une chaîne de caractères en argument.")
else:
    result = supprimer_caracteres_identiques_adjacents()
    print(result)
