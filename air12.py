# Fonctions utilisées
def array_print(array):
    for element in array:
        print(f"{element} ", end="")
    print()

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def are_numbers(array):
    return all(is_number(element) for element in array)

def array_str_to_int(array):
    result = []
    for element in array:
        result.append(int(element))
    return result

def partition(array, first, last):
    pivot = array[last]
    pIndex = first
    i = first
    while i < last:
        if int(array[i]) <= int(pivot):
            array[i], array[pIndex] = array[pIndex], array[i]
            pIndex += 1
        i += 1
    array[pIndex], array[last] = array[last], array[pIndex]
    return pIndex

def quick_sort(array, first, last):
    if first < last:
        j = partition(array, first, last)
        quick_sort(array, first, j-1)
        quick_sort(array, j+1, last)
    return array

def my_quick_sort(array):
    return quick_sort(array, 0, len(array)-1)

# Partie 1 : Gestion d'erreurs
import sys

if len(sys.argv) < 2:
    print("error: wrong number of arguments")
    sys.exit(1)

if not are_numbers(sys.argv[1:]):
    print("error: bad arguments")
    sys.exit(1)

# Partie 2 : Parsing
array = array_str_to_int(sys.argv[1:])

# Partie 3 : Résolution
result = my_quick_sort(array)

# Partie 4 : Affichage
array_print(result)
